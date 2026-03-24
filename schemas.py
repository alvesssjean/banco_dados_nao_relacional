from pydantic import BaseModel

class Car(BaseModel):
    modelo: str
    marca: str
    ano: int

