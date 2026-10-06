import functools
import connexion
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.responses import RedirectResponse
from models import Base, CpuReport, DiskLatencyReport

DB_ENGINE = create_engine("sqlite:///telemetry.db")
SessionLocal = sessionmaker(bind=DB_ENGINE)

def use_db_session(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        try:
            return func(session, *args, **kwargs)
        finally:
            session.close()
    return wrapper

@use_db_session
def report_cpu_usage(session, body):
    event = CpuReport(
        server_id=body["server_id"],
        cpu_utilization_pct=body["cpu_utilization_pct"],
        core_count=body["core_count"],
        timestamp=body["timestamp"]
    )
    session.add(event)
    session.commit()
    return NoContent, 201

@use_db_session
def report_disk_latency(session, body):
    event = DiskLatencyReport(
        server_id=body["server_id"],
        read_latency_ms=body["read_latency_ms"],
        timestamp=body["timestamp"],
        mount_point=body["mount_point"]
    )
    session.add(event)
    session.commit()
    return NoContent, 201

async def redirect_to_ui(request):
    return RedirectResponse(url="/ui")

app = connexion.AsyncApp(__name__, specification_dir="")
app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)
app.add_url_rule("/", view_func=redirect_to_ui, methods=["GET"])

if __name__ == "__main__":
    app.run(port=8090)