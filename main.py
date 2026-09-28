# main.py
from fastapi import FastAPI, HTTPException, status
from schemas import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeePatch,
    EmployeeResponse,
)
import crud

app = FastAPI(
    title="Лабораторна робота №5 — Варіант 5",
    description="REST API для обліку співробітників, що мають комп'ютер",
    version="1.0.0",
)


# ---------- GET: отримати всіх ----------
@app.get(
    "/users/",
    response_model=list[EmployeeResponse],
    summary="Отримати список усіх співробітників",
    tags=["Employees"],
)
def get_users():
    return crud.get_all_employees()


# ---------- GET: отримати одного ----------
@app.get(
    "/user/{emp_id}",
    response_model=EmployeeResponse,
    summary="Отримати співробітника за ID",
    tags=["Employees"],
)
def get_user(emp_id: int):
    emp = crud.get_employee_by_id(emp_id)
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Співробітника з id={emp_id} не знайдено",
        )
    return emp


# ---------- POST: створити ----------
@app.post(
    "/users/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Додати нового співробітника",
    tags=["Employees"],
)
def create_user(data: EmployeeCreate):
    return crud.create_employee(data)


# ---------- PUT: повне оновлення ----------
@app.put(
    "/user/{emp_id}",
    response_model=EmployeeResponse,
    summary="Повністю оновити дані співробітника",
    tags=["Employees"],
)
def update_user(emp_id: int, data: EmployeeUpdate):
    emp = crud.update_employee(emp_id, data)
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Співробітника з id={emp_id} не знайдено",
        )
    return emp


# ---------- PATCH: часткове оновлення ----------
@app.patch(
    "/user/{emp_id}",
    response_model=EmployeeResponse,
    summary="Частково оновити дані співробітника",
    tags=["Employees"],
)
def patch_user(emp_id: int, data: EmployeePatch):
    emp = crud.patch_employee(emp_id, data)
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Співробітника з id={emp_id} не знайдено",
        )
    return emp


# ---------- DELETE: видалити ----------
@app.delete(
    "/user/{emp_id}",
    response_model=EmployeeResponse,
    summary="Видалити співробітника",
    tags=["Employees"],
)
def delete_user(emp_id: int):
    emp = crud.delete_employee(emp_id)
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Співробітника з id={emp_id} не знайдено",
        )
    return emp