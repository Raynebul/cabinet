from typing import Annotated

from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import sessionmaker, Session
from router.repository import get_db, User, Material

router = APIRouter(
    prefix="/metadata",
    tags=["metadata"],
)


@router.get("/{id}")
async def get_material(id: str, db: Session = Depends(get_db)):
    material = db.query(Material).filter(Material.IDtext == id).first()
    print(material.metadata_)
    metadata = material.metadata_
    new_id = material.id
    return {"metadata": metadata, "new_id": new_id}


@router.post("/")
async def get_material(data=Body(), db: Session = Depends(get_db)):
    metadata_ = data["metadata_"]
    name = data["name"]
    id_text = data["IDtext"]
    new_material = Material(IDtext=id_text,
                            name=name,
                            metadata_=metadata_,
                            )
    print(id_text, name, metadata_)
    db.add(new_material)
    db.commit()
    db.refresh(new_material)
    return {"test": True}
