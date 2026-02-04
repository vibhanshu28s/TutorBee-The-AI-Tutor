import cv2
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# Replace 'your_video.mp4' with the path to your file
VIDEO_PATH = 'animations/bye.mp4'
camera = cv2.VideoCapture(VIDEO_PATH)

def gen_frames():
    while True:
        success, frame = camera.read()
        
        if not success:
            # If the video ends, reset the frame position to 0 (start)
            camera.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, frame = camera.read()
            if not success:
                break # Break if the file is corrupted or missing

        # Encode and yield
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/video_feed")
async def video_feed():
    return StreamingResponse(gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
     return templates.TemplateResponse("index.html", {"request": request}) 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)