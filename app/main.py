from fastapi import FastAPI
from app.routes import video
from app.routes.sensors import send_sensor_realtime, send_sensor_hourly


app = FastAPI()



app.include_router(video.video_route)

send_sensor_realtime()
send_sensor_hourly()



