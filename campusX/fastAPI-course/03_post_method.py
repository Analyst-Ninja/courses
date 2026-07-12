import json
from typing import Annotated, Literal

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
        Literal["male", "female", "others"],
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
