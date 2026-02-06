from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import animation_module.talking as am_talking
import animation_module.idle as am_idlle
import animation_module.bye as am_bye
import templates.welcome_name

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# @app.get("/video_feed")
# async def video_feed():
#     return StreamingResponse(am_bye.gen_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/welcome", response_class=HTMLResponse)
async def welcome_user(request: Request):
    #  return templates.TemplateResponse("index.html", {"request": request}) 
    return templates.welcome_name