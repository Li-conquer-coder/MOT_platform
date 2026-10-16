from sqlalchemy import Integer, String, DateTime, Column
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from db.session import Base


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False, autoincrement=True, comment='原始文件名')
    save_path: Mapped[str] = mapped_column(String(255), nullable=False, autoincrement=True, comment='保存路径')
    status: Mapped[str] = mapped_column(String(255), nullable=False, autoincrement=True, comment='保存状态')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, comment='创建时间')
