from fastapi import Depends, FastAPI
from modules import connect, crud, schemas
from sqlalchemy.orm import Session

# Initialize Database
connect.Base.metadata.create_all(bind=connect.engine)

app = FastAPI(title="Streamlit Backend API")

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.get("/items", response_model=list[schemas.Item])
def read_items(db: Session = Depends(connect.get_db)):
    return crud.get_items(db)

@app.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(connect.get_db)):
    return crud.create_item(db=db, item=item)

