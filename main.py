from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

class Persona(BaseModel):
    id: Optional[int]= None
    nombre: str
    edad: int
    email: EmailSTR

#API
from fastapi import FastAPI, HTTPException

app = FastAPI()

#Base de datos simulada
persona_db = []

#crear persona
@app.post("/personas/", response_model=Persona)
def crear_persona(persona:Persona):
    persona.id = len(persona_db)
    return persona

#Ver persona por id
@app.get("/personas/{persona_id}",response_model=Persona)
def obtener_persona(persona_id: int):
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
        raise HTTPException (status_code=404, detail="Persona no encontrada")
    
#Listar Personas
@app.get("/personas/", response_model=Persona)
def listar_personas():
    return persona_db

#Actualizar personas
@app.put("/personas/{persona_id}", response_model=Persona)
def actualizar_persona(persona_id: int, persona: Persona):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            persona_db[index] = persona
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")
#Eliminar personas
@app.delete("/personas/{persona_id}")
def borrar_persona(persona_id: int):
    for index, persona in enumerate(persona_db):
        if persona.id == persona_id:
            persona_db.pop(index)
            return {"message": "Persona eliminada"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")