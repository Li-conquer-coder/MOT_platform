from fastapi import FastAPI
from routers import video, task
from db.session import Base, get_db, engine
from models.task import Task

app = FastAPI(title="MOT Platform")

Base.metadata.create_all(bind=engine)

app.include_router(video.router)
app.include_router(task.router)


@app.get("/")
async def root():
    return {"message": "MOT平台已成功启动"}
