# crud.py
from typing import Optional
from database import employees_db, get_next_id
from schemas import EmployeeCreate, EmployeeUpdate, EmployeePatch


def get_all_employees() -> list[dict]:
    return employees_db


def get_employee_by_id(emp_id: int) -> Optional[dict]:
    for emp in employees_db:
        if emp["id"] == emp_id:
            return emp
    return None


def create_employee(data: EmployeeCreate) -> dict:
    new_emp = {
        "id": get_next_id(),
        "surname": data.surname,
        "room": data.room,
        "department": data.department,
        "computer": data.computer,
    }
    employees_db.append(new_emp)
    return new_emp


def update_employee(emp_id: int, data: EmployeeUpdate) -> Optional[dict]:
    emp = get_employee_by_id(emp_id)
    if not emp:
        return None
    emp["surname"] = data.surname
    emp["room"] = data.room
    emp["department"] = data.department
    emp["computer"] = data.computer
    return emp


def patch_employee(emp_id: int, data: EmployeePatch) -> Optional[dict]:
    emp = get_employee_by_id(emp_id)
    if not emp:
        return None
    update_data = data.model_dump(exclude_unset=True)
    emp.update(update_data)
    return emp


def delete_employee(emp_id: int) -> Optional[dict]:
    for i, emp in enumerate(employees_db):
        if emp["id"] == emp_id:
            return employees_db.pop(i)
    return None