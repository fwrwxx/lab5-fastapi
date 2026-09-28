# database.py
# Імітація БД у пам'яті
# Для лабораторної достатньо in-memory сховища.

employees_db: list[dict] = [
    {
        "id": 1,
        "surname": "Петренко",
        "room": "301",
        "department": "Кафедра ІСТ",
        "computer": "Dell OptiPlex 7090, Intel i7, 16GB RAM, SSD 512GB"
    },
    {
        "id": 2,
        "surname": "Іваненко",
        "room": "302",
        "department": "Кафедра ІСТ",
        "computer": "HP ProDesk 400 G7, Intel i5, 8GB RAM, SSD 256GB"
    },
    {
        "id": 3,
        "surname": "Сидоренко",
        "room": "305",
        "department": "Кафедра обчислювальної техніки",
        "computer": "Lenovo ThinkCentre M720, Intel i5, 16GB RAM, HDD 1TB"
    },
]

def get_next_id() -> int:
    if not employees_db:
        return 1
    return max(emp["id"] for emp in employees_db) + 1