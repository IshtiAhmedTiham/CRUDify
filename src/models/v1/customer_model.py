from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from src.config.v1.database import Base


def utc_now():
    return datetime.now(timezone.utc)

class CustomerModel(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    role = Column(String(20), nullable=False, default="cashier")
    created_at = Column(DateTime(timezone=True), default=utc_now, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utc_now, onupdate=utc_now, nullable=False)