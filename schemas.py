from pydantic import BaseModel

class Car(BaseModel):
    modelo: str
    marca: str
    ano: int

class SalesByCategory(BaseModel):
    id: str
    total: float