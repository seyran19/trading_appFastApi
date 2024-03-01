import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth.database import get_async_session
from src.operations.models import Operation
from src.operations.schemas import OperationCreate
from fastapi_cache.decorator import cache

# query - обычнно запрос на выборку
# statement or stmt - запросы на удаление вставку и т.д

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/")
@cache(expire=60)
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Operation).where(Operation.type == operation_type)  # это и есть то что мы работаем через ORM
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.first()[0].to_json(),
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {
            "status": "success",
            "data": new_operation.dict(),
            "details": None
        }
    except Exception as e:
        raise HTTPException(status_code=404, detail={
            "status": "error",
            "data": None,
            "details": None
        })


