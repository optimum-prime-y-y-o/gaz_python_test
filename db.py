from sqlalchemy import create_engine,Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Модель данных для хранения статистики устройства
class DeviceStats(Base):
    __tablename__ = "Device_stats"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(ForeignKey("Devices.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

class Devices(Base):
    __tablename__ = "Devices"

    id = Column(Integer, primary_key=True, index=True)

class UsersDevices(Base):
    __tablename__ = "Users_devices"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(ForeignKey("Devices.id"))
    user_id = Column(ForeignKey("Users.id"))

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
# Создание таблицы в базе данных
Base.metadata.create_all(bind=engine)