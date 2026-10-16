from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["任务模块"])


@router.post("/create")
async def create_task(video_path: str):
    return {"task_id": 10001, "status": "pending"}


@router.get("/{task_id}")
async def get_task(task_id: int):
    return {"task_id": task_id, "status": "processing"}
