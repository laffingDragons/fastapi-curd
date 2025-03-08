from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter()

db_dependency = Depends(database.get_db)

@router.get("/items", response_model=list[schemas.ItemResponse])
def read_items(db: Session = db_dependency):
    return crud.get_items(db)

@router.post("/items", response_model=schemas.ItemResponse)
def create_new_item(item: schemas.ItemCreate, db: Session = db_dependency):
    return crud.create_item(db, item)