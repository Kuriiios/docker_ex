from sqlalchemy.orm import Session

from . import connect, schemas


def get_items(db: Session):
    return db.query(connect.Item).all()

def create_item(db: Session, item: schemas.ItemCreate):
    # Convert Pydantic object to SQLAlchemy model
    db_item = connect.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
