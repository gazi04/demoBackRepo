from decimal import Decimal
from sqlalchemy import (
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class Customer(Base):
    __tablename__ = "customers"
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

class Order(Base):
    __tablename__ = "orders"
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    customer: Mapped[str] = mapped_column(String(255))
    ordered_at: Mapped[str] = mapped_column(String(255))
    store_id: Mapped[str] = mapped_column(String(255))
    subtotal: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    tax_paid: Mapped[int] = mapped_column(Integer)
    order_total: Mapped[int] = mapped_column(Integer)

class Item(Base):
    __tablename__ = "items"
    id: Mapped[str] = mapped_column(String(255), primary_key=True)
    order_id: Mapped[str] = mapped_column(String(255))
    sku: Mapped[str] = mapped_column(String(255))
