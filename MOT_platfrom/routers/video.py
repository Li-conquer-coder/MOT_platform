import os
import time
from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks,HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from models.task import Task
from utils.mot_runner import fake_mot_process

router = APIRouter(prefix="/video", tags=["视频模块"])


@router.post("/upload/")
async def upload_files(
        background_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    os.makedirs("uploads", exist_ok=True)

    file_extension = os.path.splitext(file.filename)[1]
    new_filename = f"{int(time.time())}{file_extension}"
    file_path = os.path.join("uploads", new_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    new_task = Task(
        filename=file.filename,
        save_path=file_path,
        status="pending"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    background_tasks.add_task(fake_mot_process, new_task.id, file_path)

    return {
        "task_id": new_task.id,
        "filename": new_task.filename,
        "status": new_task.status,
        "message": "上传成功，已入库！"
    }
@router.get("/tasks/")
async def get_all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task