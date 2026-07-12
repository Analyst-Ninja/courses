import json
from typing import Annotated, Literal, Optional

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field

app = FastAPI()


class Patient(BaseModel):
    id: Annotated[
        str, Field(..., description="ID of the patient", examples=["P001", "P002"])
    ]
    name: Annotated[
        str, Field(..., description="Name of the patient", examples=["Rohit"])
    ]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age: Annotated[int, Field(..., description="Patient's Age", gt=0, le=120)]
    gender: Annotated[
        Literal["male", "female", "other"],
        Field(..., description="Gender of the patient"),
    ]
    height: Annotated[float, Field(..., gt=0, description="Patient's height in m")]
    weight: Annotated[float, Field(..., gt=0, description="Patient's weight in kg")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round((self.weight / (self.height**2)), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25.0:
            return "Normal"
        elif self.bmi < 30.0:
            return "Overweight"
        else:
            return "Obese"


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, le=120)]
    gender: Annotated[Optional[Literal["male", "female", "other"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)


def save_data(data):
    with open("patients.json", "w") as file:
        json.dump(data, file)


@app.get("/")
def root():
    return {"message": "Patient Management System"}


@app.get("/about")
def about():
    return {"message": "Fully functional API to manage Patient records"}


@app.get("/view")
def view():
    return load_data()


@app.get("/patient/{patient_id}/")
def view_patient(
    patient_id: str = Path(
        ...,
        title="Patient ID",
        description="ID of the patient in the patient data",
        example="P001",
    ),
):
    # load all patients data
    data = load_data()
    if patient_id in data:
        return {"message": data[patient_id]}
    raise HTTPException(status_code=404, detail=f"data not found with id {patient_id}")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: str = Query(default="asc", description="Ascending or Descending"),
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field, select from valid fields - {valid_fields}",
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Select between asc or desc")

    data = load_data()

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=("desc" == order)
    )

    return sorted_data


@app.post("/create")
def create_patient(patient: Patient):
    # load existing data
    data = load_data()

    # check if the patient already exits, raise error
    if patient.id in data:
        raise HTTPException(
            status_code=400, detail=f"Patient already exists with id - {patient.id}"
        )

    # if new patient, add new patient
    else:
        data[patient.id] = patient.model_dump(exclude=["id"])

    # Save data
    save_data(data=data)

    return JSONResponse(
        status_code=201,
        content={"message": f"Patient created successfully with id - {patient.id}"},
    )


@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(
            status_code=404, detail=f"Patient not found with {patient_id}"
        )

    existing_patient_info = data[patient_id]

    new_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, val in new_patient_info.items():
        existing_patient_info[key] = val

    # Convert it into Pateint Pydantic obj to create get the bmi and verdit as well
    # But we need to add the id key as well
    existing_patient_info["id"] = patient_id

    # create patient Pydantic obj
    updated_patient_obj = Patient(**existing_patient_info)

    # Add the updated data using model_dump to the dictionary
    data[patient_id] = updated_patient_obj.model_dump(exclude=["id"])

    # save data to JSON
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={"message": f"Patient info has been updated with id - {patient_id}"},
    )


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    # load data
    data = load_data()

    # check if the patient exists
    if patient_id not in data:
        raise HTTPException(
            status_code=404, detail=f"Patient does not exists with id - {patient_id}"
        )

    # Exclude the patient data with given patient id
    del data[patient_id]

    # data = {k: v for k, v in data.items() if k != patient_id}

    # Save the data
    save_data(data=data)

    return JSONResponse(
        status_code=202, content={"message": f"Patient deleted with id - {patient_id}"}
    )
