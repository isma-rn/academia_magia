from sqlalchemy.orm import Session
from sqlalchemy import update
from . import models, schemas
import random

def get_estudiante_por_identificacion(db: Session, identificacion: str):
    return db.query(models.Solicitud).filter(models.Solicitud.identificacion == identificacion).first()

def create_solicitud(db: Session, solicitud: schemas.SolicitudCreate):    
    db_solicitud = models.Solicitud(nombre=solicitud.nombre,apellido=solicitud.apellido,identificacion=solicitud.identificacion,edad=solicitud.edad,afinidad=solicitud.afinidad,estatus="PROCESO")
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud

def get_solicitud(db: Session):
    return db.query(models.Solicitud).all()

def get_solicitud_por_id(db: Session, id: int):
    return db.query(models.Solicitud).filter(models.Solicitud.id == id).first()

def edit_solicitud(db: Session, id: int, solicitud: schemas.SolicitudCreate):
    consulta_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == id).first()
    consulta_solicitud.nombre = solicitud.nombre
    consulta_solicitud.apellido = solicitud.apellido
    consulta_solicitud.edad = solicitud.edad
    consulta_solicitud.afinidad = solicitud.afinidad
    db.commit()
    db.refresh(consulta_solicitud)
    return consulta_solicitud

def actualiza_estatus(db: Session, id: int, estatus: str):
    consulta_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == id).first()
    consulta_solicitud.estatus = estatus
    if(estatus.upper() == "APROBADA"):
        trevol = random.randint(1, 5)
        consulta_solicitud.grimorio = f"Trevol {trevol} hoja(s)"
    db.commit()
    db.refresh(consulta_solicitud)
    return consulta_solicitud


def delete_solicitud(db: Session, id: int):
    consulta_solicitud = db.query(models.Solicitud).filter(models.Solicitud.id == id).first()
    db.delete(consulta_solicitud)
    db.commit()
    
    return consulta_solicitud