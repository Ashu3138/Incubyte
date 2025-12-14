from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetUpdate
from app.core.dependencies import get_db, get_current_user, admin_only

router = APIRouter(prefix="/api/sweets", tags=["Sweets"])

@router.post("/", dependencies=[Depends(admin_only)])
def add_sweet(data: SweetCreate, db: Session = Depends(get_db)):
    sweet = Sweet(**data.dict())
    db.add(sweet)
    db.commit()
    return sweet

@router.get("/", dependencies=[Depends(get_current_user)])
def list_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()

@router.post("/{id}/purchase", dependencies=[Depends(get_current_user)])
def purchase(id: int, db: Session = Depends(get_db)):
    sweet = db.query(Sweet).get(id)
    if not sweet or sweet.quantity <= 0:
        raise HTTPException(400, "Out of stock")
    sweet.quantity -= 1
    db.commit()
    return sweet
