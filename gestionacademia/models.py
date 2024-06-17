from sqlalchemy import Column, Integer, String
from .database import Base

class Solicitud(Base):
    __tablename__ = "solicitud"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(20), index=True)
    apellido = Column(String(20))
    identificacion = Column(String(10))
    edad = Column(Integer)
    afinidad = Column(String(20))
    grimorio = Column(String(20), nullable=True)
    estatus = Column(String(20))