# cd example2 - перейти в папку
# uvicorn server:app --reload - запустить фаил с перезагрузкой изменений

from enum import Enum
import random
from typing import Optional, List
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="New App with FastAPI",
    description="new application by Vadim Sidorenko",
)

# https://docs.pydantic.dev/latest/usage/types/


class TypeEquipment(Enum):
    classic = "Classic"
    comfort = "Comfort"
    luxe = "Luxe"
    prestige = "Prestige"
    premium = "Premium"


class Equipment(BaseModel):
    id: int
    type_equipment: TypeEquipment


class Car(BaseModel):
    # проверка на значение больше или равно 0
    serial_key: int = Field(ge=0)
    car_id: int
    car_name = str
    car_model: str = Field(max_length=10)
    car_color: Optional[List[str]] = ["FFF000"]
    car_equipment: List[Equipment] = []
    date_of_purchase: Optional[datetime] = None


external_data = [
    {
        'serial_key': 1,
        'car_id': 22,
        'car_name': 'Lada Granda',
        'car_model': 'Sedan',
        'car_color': ["000000"],
        'car_equipment': [
            {
                "id": 2,
                "type_equipment": TypeEquipment.classic
            }
        ],
        'date_of_purchase': '2019-06-01 12:22',
    }
]

# имуляция клиента
for user in range(5):
    randInt = random.randint(1, 10)
    randIntSum = randInt + random.randint(1, 10)
    id = randInt
    user: List[Car] = {
        'serial_key': randIntSum,
        'car_id': randInt,
        'car_name': 'Lada Granda',
        'car_model': 'Sedan',
        'car_color': ["FFF000", "000000", "FF00FF", "00FF00"],
        'car_equipment': [{
            "id": 1,
            "type_equipment": TypeEquipment.premium
        }],
        'date_of_purchase': '2019-06-01 12:22',
    }
    external_data.append(user)


@app.post("/users/add-external-data")
async def add_external_data(external: List[Car]):
    external_data.extend(external)
    return {"status": 200, "data": external_data}
