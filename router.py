from fastapi import FastAPI, HTTPException, Path
from typing import List, Optional, Annotated
from datetime import datetime
from DAO import DeviceStatsDAO
import uvicorn
from DAO import DeviceStatCreate

app = FastAPI()


# получаем статистику
@app.post("/devices/{device_id}/stats/")
def create_device_stat(device_id: str, stat: DeviceStatCreate):
    
    DeviceStatsDAO.insert_data(device_id,stat)
    return {"message": "Device stat created successfully"}

# отправляем статистику 
@app.get("/devices/{device_id}/stats/")
def get_device_stats(device_id: Annotated[int, Path(title="The ID of the device to get", gt=0)], 
                     start_date: Optional[datetime] = None, 
                     end_date: Optional[datetime] = None):
    res = DeviceStatsDAO.find_data(device_id,start_date,end_date)
    print(type(res),res)
    if res == []:
        raise HTTPException(status_code=404, detail="data not found")
    else:
        return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
