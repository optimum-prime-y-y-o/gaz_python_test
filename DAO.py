# from app.dao.base import BaseDao
from db import DeviceStats
from db import SessionLocal #async_session_maker
from sqlalchemy import insert, select, update, func
from datetime import datetime
import pandas as pd
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel

class DeviceStatCreate(BaseModel):
    x: float
    y: float
    z: float

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id:int):
        async with SessionLocal() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

class DeviceStatsDAO(BaseDAO):
    model = DeviceStats

    #@classmethod
    def find_data(device_id:int,
                  start_date:datetime,
                  end_date:datetime):
        with SessionLocal() as session:   
            # res = session.query(DeviceStats). \
            # filter(DeviceStats.device_id==device_id,
            #                         DeviceStats.timestamp > start_date,
            #                         DeviceStats.timestamp < end_date)
            if start_date and end_date:
                print("1")
                res = session.query(DeviceStats). \
                            filter(DeviceStats.device_id==device_id,
                                    DeviceStats.timestamp > start_date,
                                    DeviceStats.timestamp < end_date)
            elif start_date:
                print("2")
                res = session.query(DeviceStats). \
                                filter(DeviceStats.device_id==device_id,
                                    DeviceStats.timestamp > start_date)
            elif end_date:
                print("3")
                res = session.query(DeviceStats). \
                                filter(DeviceStats.device_id==device_id,
                                    DeviceStats.timestamp < end_date)
            else:
                print("4")
                res = session.query(DeviceStats). \
                                filter(DeviceStats.device_id==device_id)
                
            df = pd.read_sql(res.statement, res.session.bind)
            # получаем мин, макс, количество, сумму, медиану по x,y,z
            aggregation = {"x":["min","max","count","sum","median"],
                           "y":["min","max","count","sum","median"],
                           "z":["min","max","count","sum","median"]}

            df2=df.groupby(["device_id"]).agg(aggregation).reset_index()
            df2.columns = ['_'.join(col) for col in df2.columns]
            res = df2.to_json(orient="records")
            parsed = json.loads(res)
            return parsed
    
    def insert_data(device_id:int,stat: DeviceStatCreate):
        with SessionLocal() as session:

            query = insert(DeviceStats).values(
                device_id=device_id,
                x=stat.x,
                y=stat.y,
                z=stat.z,
                timestamp = datetime.now()
            )
            
            result = session.execute(query)
            session.commit()
            return result