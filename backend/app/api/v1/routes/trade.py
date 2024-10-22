from app.core.user_balance import USER_BALANCE
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.trade import TradeRead, TradeCreate
from app.services.trade_service import get_user_trades_per_event, create_trade, get_user_trades, get_trade_by_id
from app.services.user_service import get_current_user
from app.models.user import User
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

    # Validate offer_type and order_type
    if offer_type not in ["buy", "sell"]:
        raise HTTPException(status_code=400, detail="Invalid offer type")
    if order_type not in ["LO", "MO"]:
        raise HTTPException(status_code=400, detail="Invalid order type")
    price = l1_expected_price*100
    USER_BALANCE.lockBalance(current_user.id, l1_order_quantity*price)
    print(USER_BALANCE.data)

    # Here you would typically call a service function to handle the order
    # For example:
    # result = trade_service.initiate_order(
    #     user_id=current_user.id,
    #     event_id=event_id,
    #     offer_type=offer_type,
    #     order_type=order_type,
    #     quantity=l1_order_quantity,
    #     price=l1_expected_price
    # )
    
    # For now, we'll just return a dummy response
    return {
        "status": "success",
        "message": "Order initiated successfully",
        "order_details": order_data
    }