# Validação
from pydantic import BaseModel

# Modelo para criação
class TaskCreate(BaseModel):
    title: str
    description: str

# Modelo para retorno
class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True  # Permite que o Pydantic leia dados do ORM