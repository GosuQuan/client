from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, case
from typing import Dict, Any
from app.db.session import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.task import Task
from app.models.focus_session import FocusSession
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/stats", response_model=Dict[str, Any])
async def get_dashboard_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取仪表盘统计数据"""
    # 获取专注会话统计
    focus_stats = db.query(
        func.count(FocusSession.id).label('total_focus'),
        func.sum(FocusSession.duration).label('total_time')
    ).filter(
        FocusSession.user_id == current_user.id
    ).first()

    # 获取任务统计
    task_stats = db.query(
        func.count(Task.id).label('total_tasks'),
        func.sum(case((Task.completed == True, 1), else_=0)).label('completed_tasks')
    ).filter(
        Task.user_id == current_user.id
    ).first()

    # 格式化总时间
    total_minutes = focus_stats.total_time or 0
    hours = total_minutes // 60
    minutes = total_minutes % 60
    time_str = f"{hours}h {minutes}m" if minutes else f"{hours}h"

    return {
        "totalFocus": focus_stats.total_focus or 0,
        "totalTime": time_str,
        "totalTasks": task_stats.total_tasks or 0,
        "completedTasks": task_stats.completed_tasks or 0
    }

@router.get("/focus-history")
async def get_focus_history(
    days: int = 7,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取专注历史数据"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    focus_history = db.query(
        func.date(FocusSession.start_time).label('date'),
        func.count(FocusSession.id).label('sessions'),
        func.sum(FocusSession.duration).label('total_duration')
    ).filter(
        FocusSession.user_id == current_user.id,
        FocusSession.start_time >= start_date,
        FocusSession.start_time <= end_date
    ).group_by(
        func.date(FocusSession.start_time)
    ).all()

    return [{
        "date": entry.date.strftime("%Y-%m-%d"),
        "sessions": entry.sessions,
        "duration": entry.total_duration
    } for entry in focus_history]

@router.get("/task-stats")
async def get_task_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取任务统计数据"""
    # 按状态统计任务
    task_by_status = db.query(
        Task.status,
        func.count(Task.id).label('count')
    ).filter(
        Task.user_id == current_user.id
    ).group_by(
        Task.status
    ).all()

    # 按优先级统计任务
    task_by_priority = db.query(
        Task.priority,
        func.count(Task.id).label('count')
    ).filter(
        Task.user_id == current_user.id
    ).group_by(
        Task.priority
    ).all()

    return {
        "byStatus": [{
            "status": status,
            "count": count
        } for status, count in task_by_status],
        "byPriority": [{
            "priority": priority,
            "count": count
        } for priority, count in task_by_priority]
    }
