# schemas.py
from pydantic import BaseModel, Field
from typing import Optional

class EmployeeBase(BaseModel):
    surname: str = Field(..., min_length=2, max_length=50, description="Прізвище співробітника")
    room: str = Field(..., min_length=1, max_length=10, description="Номер кімнати")
    department: str = Field(..., min_length=2, max_length=100, description="Назва відділу")
    computer: str = Field(..., min_length=2, max_length=200, description="Дані про комп'ютер")

class EmployeeCreate(EmployeeBase):
    """Схема для створення (POST)"""
    pass

class EmployeeUpdate(BaseModel):
    """Схема для повного оновлення (PUT) — всі поля обов'язкові"""
    surname: str = Field(..., min_length=2, max_length=50)
    room: str = Field(..., min_length=1, max_length=10)
    department: str = Field(..., min_length=2, max_length=100)
    computer: str = Field(..., min_length=2, max_length=200)

class EmployeePatch(BaseModel):
    """Схема для часткового оновлення (PATCH) — всі поля опціональні"""
    surname: Optional[str] = Field(None, min_length=2, max_length=50)
    room: Optional[str] = Field(None, min_length=1, max_length=10)
    department: Optional[str] = Field(None, min_length=2, max_length=100)
    computer: Optional[str] = Field(None, min_length=2, max_length=200)

class EmployeeResponse(EmployeeBase):
    """Схема відповіді"""
    id: int

    class Config:
        from_attributes = True