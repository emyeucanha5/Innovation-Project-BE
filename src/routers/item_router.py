from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Body, Depends, Form, Security, File, UploadFile
from fastapi.params import Path
from schemas.item.request_dto import CreateItemRequestDto
from schemas.item.response_dto import (
    CreateItemResponseDto,
    GetAnItemResponseDto,
)
from services.item_service import ItemService
from starlette import status
from utils.auth import get_current_user

router = APIRouter(
    prefix="/items",
    tags=["Item"],
)
item_service = ItemService()


@router.post(
    "/create-item",
    status_code=status.HTTP_200_OK,
    response_model=CreateItemResponseDto,
)
async def create_new_item(
    payload: CreateItemRequestDto = Body(...),
    item_file: UploadFile = File(None),
    user: dict = Depends(get_current_user),
):
    return item_service.create_item(payload, item_file, user)


@router.get(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetAnItemResponseDto,
)
async def get_an_item(
    item_id: str = Path(
        ...,
        title="item_id",
        example="1",
    ),
):
    return item_service.get_an_item(item_id)
