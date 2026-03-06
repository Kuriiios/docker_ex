from models import models
from sqlalchemy.orm import Session

from modules import connect


def get_items(db: Session):
    return db.query(connect.Item).all()

def create_item(db: Session, item: models.ItemCreate):
    # Convert Pydantic object to SQLAlchemy model
    db_item = connect.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
