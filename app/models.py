# Modelo BD
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

# Tabela
class Task(Base):
    __tablename__ = "tasks"
    
    # Estrutura
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    completed = Column(Boolean, default=False)