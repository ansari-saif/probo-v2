from app.core.common_utils import publish_queue, subscribe_queue
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.trade import TradeRead, TradeCreate
from app.services.trade_service import  create_trade, get_user_trades
from app.services.user_service import get_current_user
from app.models.user import User
from app.core.constraints import RABBITMQ_QUEUE
import asyncio

router = APIRouter()

@router.post("/trades", response_model=TradeRead, status_code=status.HTTP_201_CREATED)
async def create_new_trade(
    trade: TradeCreate, 
    current_user: User = Depends(get_current_user)
):
    new_trade = create_trade(trade, current_user.id)
    if not new_trade:
        raise HTTPException(status_code=400, detail="Failed to create trade")
    return new_trade

@router.get("/trades", response_model=List[TradeRead])
async def read_user_trades(
    skip: int = 0, 
    limit: int = 100, 
    current_user: User = Depends(get_current_user)
):
    trades = get_user_trades(current_user.id, skip=skip, limit=limit)
    return trades

@router.post("/oms/order/initiate")
async def initiate_order(
    order_data: dict,
    current_user: User = Depends(get_current_user)
):
    # Extract data from request body
    event_id = order_data.get("event_id")
    offer_type = order_data.get("offer_type")
    order_type = order_data.get("order_type")
    l1_order_quantity = order_data.get("l1_order_quantity")
    l1_expected_price = order_data.get("l1_expected_price")

    # Validate required fields
    if not all([event_id, offer_type, order_type, l1_order_quantity, l1_expected_price]):
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    # TODO : I've to read this 
    # order_status_future = asyncio.Future()

    # Validate offer_type and order_type
    if offer_type not in ["BUY", "SELL"]:
        raise HTTPException(status_code=400, detail="Invalid offer type")
    if order_type not in ["LO", "MO"]:
        raise HTTPException(status_code=400, detail="Invalid order type")

    data_to_publish = {
        "event_id": event_id,
        "user_id": current_user.id,
        "offer_type": offer_type,
        "l1_expected_price": l1_expected_price,
        "l1_order_quantity": l1_order_quantity,
        "is_reverse": False
    }
    order_status_future = asyncio.create_task(subscribe_queue(current_user.id))

    publish_queue(data_to_publish, RABBITMQ_QUEUE)
    try:
        order_status = await asyncio.wait_for(order_status_future, timeout=5.0)
        print(order_status_future)
    except asyncio.TimeoutError:
        order_status = "Pending"  # Default status if no response is received in time

    return {
        "status": order_status,
        "message": "Order initiated successfully",
        "order_details": order_data
    }
