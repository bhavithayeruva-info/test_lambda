from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -------- Employee Model --------
class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: float

# In-memory database (demo purpose)
employees: List[Employee] = []

# -------- CREATE Employee --------
@app.post("/employees")
def create_employee(emp: Employee):
    employees.append(emp)
    return {
        "message": "Employee created successfully",
        "employee": emp
    }

# -------- READ All Employees --------
@app.get("/employees")
def get_all_employees():
    return employees

# -------- READ Employee by ID --------
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            return emp
    return {"error": "Employee not found"}

# -------- UPDATE Employee --------
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, updated_emp: Employee):
    for index, emp in enumerate(employees):
        if emp.id == emp_id:
            employees[index] = updated_emp
            return {
                "message": "Employee updated successfully",
                "employee": updated_emp
            }
    return {"error": "Employee not found"}

# -------- DELETE Employee --------
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    for emp in employees:
        if emp.id == emp_id:
            employees.remove(emp)
            return {"message": "Employee deleted successfully"}
    return {"error": "Employee not found"}

# -------- Lambda Handler --------
handler = Mangum(app)
