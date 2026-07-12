from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):

    name: str = "Rohit"  # Default Values
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        ge=0,
        le=10,
        default=5.0,
        description="A decimal value representing CGPA of the student.",
    )  # Applying Constraints using Field


new_student = {
    "age": "28",  # type coercing --> will try to convert it into int
    "email": "abc@openai.com",
}

student = Student(**new_student)

# print(student, type(student))

student_dict = student.model_dump()
student_json = student.model_dump_json()

print(student_dict)
print(student_dict["name"])

print(student_json, type(student_json))
