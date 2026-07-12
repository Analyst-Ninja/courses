import json

from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()


def load_data():
    with open("patients.json", "r") as file:
        return json.load(file)


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
