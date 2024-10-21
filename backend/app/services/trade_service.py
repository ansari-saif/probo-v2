from sqlmodel import Session, select
from app.core.database import engine
from app.models.trade import Trade, TradeCreate
from typing import List, Optional

def get_user_trades_per_event(event_id: int, user_id: int) -> List[Trade]:
    with Session(engine) as session:
        statement = select(Trade).where(Trade.event_id == event_id, Trade.user_id == user_id)
        trades = session.exec(statement).all()
    return trades

def create_trade(trade: TradeCreate, user_id: int) -> Trade:
    with Session(engine) as session:
       db_trade = Trade(
        event_id=trade.event_id,
        prediction=trade.prediction,
        amount_staked=trade.amount_staked,
        user_id=user_id
    )
    session.add(db_trade)
    session.commit()
    session.refresh(db_trade)
    return db_trade

def get_user_trades(user_id: int, skip: int = 0, limit: int = 100) -> List[Trade]:
    with Session(engine) as session:
        statement = select(Trade).where(Trade.user_id == user_id).offset(skip).limit(limit)
        trades = session.exec(statement).all()
    return trades

def get_trade_by_id(trade_id: int, user_id: int) -> Optional[Trade]:
    with Session(engine) as session:
        statement = select(Trade).where(Trade.id == trade_id, Trade.user_id == user_id)
        trade = session.exec(statement).first()
    return trade
