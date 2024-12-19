from fastapi import FastAPI, HTTPException
from google.cloud import bigquery
from pydantic import BaseModel
import datetime

app = FastAPI()
client = bigquery.Client()


# Pydantic model to validate incoming data
class MetricData(BaseModel):
    timestamp: datetime.datetime
    metric_name: str
    metric_value: float


@app.post("/ingest")
async def ingest_data(metric: MetricData):
    table_id = "api-project-zzm.campaign_data.campaign_metrics"
    rows_to_insert = [
        {
            "timestamp": metric.timestamp.isoformat(),
            "metric_name": metric.metric_name,
            "metric_value": metric.metric_value,
        }
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        # If something goes wrong, report it
        raise HTTPException(status_code=500, detail=str(errors))
    return {"status": "success"}
