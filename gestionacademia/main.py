from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

lista_afinidad = ["ORCURIDAD","LUZ","FUEGO","AGUA","VIENTO","TIERRA"]
lista_estatus = ["PROCESO","RECHAZADA","APROBADA"]

@app.post("/solicitud/", response_model=schemas.Solicitud)
def create_solicitud(solicitud: schemas.SolicitudCreate, db: Session = Depends(get_db)):
    #validacion datos
    if not solicitud.identificacion or len(solicitud.identificacion)>10:
        raise HTTPException(status_code=400, detail="Identificación no válida")
    if not solicitud.nombre or len(solicitud.nombre)>20:
        raise HTTPException(status_code=400, detail="Nombre no válido")
    if not solicitud.apellido or len(solicitud.apellido)>20:
        raise HTTPException(status_code=400, detail="Apellido no válido")
    if solicitud.edad<1 or solicitud.edad>99:
        raise HTTPException(status_code=400, detail="Edad no válido")
    if not solicitud.afinidad or not solicitud.afinidad.upper() in lista_afinidad:
        raise HTTPException(status_code=400, detail="Afinidad no válida")
    
    db_estudiante = crud.get_estudiante_por_identificacion(db, identificacion=solicitud.identificacion)    
    if db_estudiante:
        raise HTTPException(status_code=400, detail="Solicitud ya registrada")
    
    return crud.create_solicitud(db=db, solicitud=solicitud)

@app.put("/solicitud/{id}", response_model=schemas.Solicitud)
def edit_solicitud(id: int, solicitud: schemas.SolicitudEdit, db: Session = Depends(get_db)):
    db_solicitud = crud.get_solicitud_por_id(db, id)
    if not db_solicitud:
        raise HTTPException(status_code=400, detail="Solicitud no encontrada")    
    if not solicitud.nombre or len(solicitud.nombre)>20:
        raise HTTPException(status_code=400, detail="Nombre no válido")
    if not solicitud.apellido or len(solicitud.apellido)>20:
        raise HTTPException(status_code=400, detail="Apellido no válida")
    if solicitud.edad<1 or solicitud.edad>99:
        raise HTTPException(status_code=400, detail="Edad no válido")
    if not solicitud.afinidad or not solicitud.afinidad.upper() in lista_afinidad:
        raise HTTPException(status_code=400, detail="Afinidad no válida")
    
    return crud.edit_solicitud(db=db, id=id, solicitud=solicitud)

@app.patch("/solicitud/{id}/{estatus}")
def edit_estatus(id: int, estatus: str, db: Session = Depends(get_db)):
    db_solicitud = crud.get_solicitud_por_id(db, id)
    if not db_solicitud:
        raise HTTPException(status_code=400, detail="Solicitud no encontrada")        
    if not estatus or not estatus.upper() in lista_estatus:
        raise HTTPException(status_code=400, detail="Estatus no válido")
    
    response = crud.actualiza_estatus(db=db, id=id, estatus=estatus)

    if not response:
        return {"message": "Error"}
    return {"message": "Estatus actualizado"}

@app.get("/solicitud/", response_model=List[schemas.Solicitud])
def read_solicitudes(db: Session = Depends(get_db)):
    solicitudes = crud.get_solicitud(db)
    return solicitudes

@app.get("/asignaciones/", response_model=List[schemas.EstudianteGrimorio])
def read_grimorios(db: Session = Depends(get_db)):
    estudiantes = crud.get_solicitud(db)
    return estudiantes

@app.delete("/solicitud/{id}")
def delete_solicitud(id: int, db: Session = Depends(get_db)):
    db_solicitud = crud.get_solicitud_por_id(db, id)
    if not db_solicitud:
        raise HTTPException(status_code=400, detail="Solicitud no encontrada")        

    crud.delete_solicitud(db=db, id=id)    
    
    return {"message": "Solicitud eliminada"}

#if __name__ == "__main__":
	#import uvicorn
	# Run the FastAPI application using Uvicorn
	#uvicorn.run(app, host="127.0.0.1", port=8000)