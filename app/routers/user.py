from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.user import get_users, get_user, create_user, update_user, delete_user
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.dependencies import get_db

# "/users"

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# GET "/users"
@router.get("/", response_model=list[UserRead])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

# GET "/users/{user_id}"
@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# POST "/users"
@router.post("/", response_model=UserRead, status_code=201)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

# PUT "/users/{user_id}"
@router.put("/{user_id}", response_model=UserRead)
async def update_existing_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    updated_user = await update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# DELETE "/users/{user_id}"
@router.delete("/{user_id}", response_model=UserRead)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted_user = await delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
