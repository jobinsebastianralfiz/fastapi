from db.repository.user import create_new_user
from db.sessions import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from schemas.user import ShowUser
from schemas.user import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
