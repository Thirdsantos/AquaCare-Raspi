import cv2
from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from run import aquarium

video_route = APIRouter()

cap = cv2.VideoCapture(0)
on_off = True




class SwitchRequest(BaseModel):
    switch: bool

@video_route.post(f"/aquarium/{aquarium}/camera_switch")
def camera_switch(data: SwitchRequest):
    global on_off
    on_off = data.switch
    return {"camera_on": on_off}

  


def open_camera():
  while on_off:
    success, frame = cap.read()
    if not success:
        break
     
    ret, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()
        
       
    yield (b'--frame\r\n'
    b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
  cap.release() 

@video_route.get(f"/aquarium/{aquarium}/video_feed")
def video_feed():
  return StreamingResponse(open_camera(), media_type="multipart/x-mixed-replace; boundary=frame")   