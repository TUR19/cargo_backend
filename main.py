from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DB, TrackCode
from pydantic import BaseModel


DATABASE_URL = "sqlite:///./DBTrackCodes.db"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DB.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TrackCodeCreate(BaseModel):
    trackCode: int
    dateRegistrationClient: bool
    receivedInStockInChina: bool
    receivedAtTheWarehouseInAlmaty: bool
    receivedByTheClient: bool


# CRUD for TrackCodes
@app.post("/trackCodes/", response_model=TrackCodeCreate)
def create_track_code(tCode: TrackCodeCreate, db: Session = Depends(get_db)):
    db_track_code = TrackCode(trackCode=tCode.trackCode, dateRegistrationClient=tCode.dateRegistrationClient, receivedInStockInChina=tCode.receivedInStockInChina, receivedAtTheWarehouseInAlmaty=tCode.receivedAtTheWarehouseInAlmaty, receivedByTheClient=tCode.receivedByTheClient)
    db.add(db_track_code)
    db.commit()
    db.refresh(db_track_code)
    return db_track_code


@app.get("/trackCodes/{track_code}")
def read_track_code(track_code: int, db: Session = Depends(get_db)):
    the_condition_of_the_product = db.query(TrackCode).filter(TrackCode.trackCode == track_code).first()
    if the_condition_of_the_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return the_condition_of_the_product


@app.patch("/trackCodes/{track_code}")
def update_track_code(track_code: int, tCode: TrackCodeCreate, db: Session = Depends(get_db)):
    the_condition_of_the_product = db.query(TrackCode).filter(TrackCode.trackCode == track_code).first()
    if the_condition_of_the_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    the_condition_of_the_product.dateRegistrationClient = tCode.dateRegistrationClient
    the_condition_of_the_product.receivedInStockInChina = tCode.receivedInStockInChina
    the_condition_of_the_product.receivedAtTheWarehouseInAlmaty = tCode.receivedAtTheWarehouseInAlmaty
    the_condition_of_the_product.receivedByTheClient = tCode.receivedByTheClient
    db.commit()
    db.refresh(the_condition_of_the_product)
    return the_condition_of_the_product


@app.delete("/trackCodes/{track_code}")
def delete_track_code(track_code: int, db: Session = Depends(get_db)):
    the_condition_of_the_product = db.query(TrackCode).filter(TrackCode.trackCode == track_code).first()
    if the_condition_of_the_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(the_condition_of_the_product)
    db.commit()
    return {"ok": True}