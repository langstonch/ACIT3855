from datetime import datetime, UTC
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DateTime

class Base(DeclarativeBase):
    pass

class CpuReport(Base):
    __tablename__ = "cpu_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    server_id: Mapped[str] = mapped_column(String(50))
    cpu_utilization_pct: Mapped[float] = mapped_column(Float)
    core_count: Mapped[int] = mapped_column(Integer)
    timestamp: Mapped[str] = mapped_column(String(50))
    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))

class DiskLatencyReport(Base):
    __tablename__ = "disk_latency_reports"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    server_id: Mapped[str] = mapped_column(String(50))
    read_latency_ms: Mapped[float] = mapped_column(Float)
    timestamp: Mapped[str] = mapped_column(String(50))
    mount_point: Mapped[str] = mapped_column(String(50))
    date_created: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(UTC))