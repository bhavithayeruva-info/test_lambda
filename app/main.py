from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: float

employees: List[Employee] = []

@app.get("/")
def root():
    return {"message": "API is working"}

@app.post("/employees")
def create_employee(emp: Employee):
    employees.append(emp)
    return emp

@app.get("/employees")
def get_all_employees():
    return employees

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    return {"detail": "Employee not found"}

@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    for i, emp in enumerate(employees):
        if emp.id == emp_id:
            employees[i] = updated_emp
            return updated_emp
    return {"detail": "Employee not found"}

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            return {"message": "Employee deleted"}
    return {"detail": "Employee not found"}

handler = Mangum(app, lifespan="off")
