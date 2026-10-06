import connexion
import requests
from connexion import NoContent
from starlette.responses import RedirectResponse

STORAGE_SERVICE_URL = "http://localhost:8090"

def report_cpu_usage(body):
    response = requests.post(
        f"{STORAGE_SERVICE_URL}/reports/cpu",
        json=body,
        headers={"Content-Type": "application/json"}
    )
    return NoContent, response.status_code

def report_disk_latency(body):
    response = requests.post(
        f"{STORAGE_SERVICE_URL}/reports/disk-latency",
        json=body,
        headers={"Content-Type": "application/json"}
    )
    return NoContent, response.status_code

async def redirect_to_ui(request):
    return RedirectResponse(url="/ui")

app = connexion.AsyncApp(__name__, specification_dir="")
app.add_api("openapi.yaml", strict_validation=True, validate_responses=True)
app.add_url_rule("/", view_func=redirect_to_ui, methods=["GET"])

if __name__ == "__main__":
    app.run(port=8080)