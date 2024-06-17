from pydantic import BaseModel

class Solicitud(BaseModel):
    id: int
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad: str
    grimorio: str | None="No asignado"
    estatus: str | None="No asignado"

class SolicitudCreate(BaseModel):
    nombre: str
    apellido: str
    identificacion: str
    edad: int
    afinidad: str

class SolicitudEdit(BaseModel):
    nombre: str
    apellido: str
    edad: int
    afinidad: str

class EstudianteGrimorio(BaseModel):
    nombre: str
    apellido: str
    grimorio: str