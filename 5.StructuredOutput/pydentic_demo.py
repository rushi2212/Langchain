#pip install email-validator
#pip install pydantic

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=9, description='CGPA of the student')  ##ge: greater than equal to, le: less than equal to
    #name: str = 'Rushikesh' ##default value

new_student = {"name":"Rushikesh Raut", "age":24, "email":"rushikesh@example.com", "cgpa":9.1}
student = Student(**new_student)
print(student)

student_dict = dict(student)  ##dict() is used to convert pydantic object to dictionary
print(student_dict['email'])

# student_dict = student.model_dump()  ##model_dump() is used to convert pydantic object to dictionary
# print(student_dict)

student_json = student.model_dump_json()  ##model_dump_json() is used to convert pydantic object to json
print(student_json)

print(type(student)) ##pydantic object