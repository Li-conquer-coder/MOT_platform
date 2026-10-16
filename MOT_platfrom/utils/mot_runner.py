import time
from db.session import Sessionlocal
from models.task import Task


def fake_mot_process(task_id: int, video_path: str):
    db = Sessionlocal()
    try:
        task = db.query(Task).filter(Task.id == task_id).first()
        if task:
            task.status = "processing"
            db.commit()
        time.sleep(5)

        if task:
            task.status = "completed"
            db.commit()
    except Exception as e:
        if task:
            task.status = "failed"
            db.commit()

    finally:
        db.close()
