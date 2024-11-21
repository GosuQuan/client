from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import schemas, models
from app.db.session import get_db
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[schemas.Task])
def list_tasks(
    skip: int = 0,
    limit: int = 100,
    status: Optional[models.TaskStatus] = None,
    priority: Optional[models.TaskPriority] = None,
    db: Session = Depends(get_db)
):
    """获取任务列表，支持状态和优先级过滤"""
    query = db.query(models.Task)
    
    if status:
        query = query.filter(models.Task.status == status)
    if priority:
        query = query.filter(models.Task.priority == priority)
        
    tasks = query.offset(skip).limit(limit).all()
    return tasks

@router.post("/", response_model=schemas.Task)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    """创建新任务"""
    # 临时使用固定用户ID，实际应该从认证中获取
    user_id = 1
    
    db_task = models.Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/{task_id}", response_model=schemas.Task)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    """获取特定任务的详细信息"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db)
):
    """更新任务"""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    """删除任务"""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(db_task)
    db.commit()
    return {"status": "success"}
