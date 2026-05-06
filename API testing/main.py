import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Crop Metrics API")

fake_db = {}

class CropMetric(BaseModel):
    region: str
    nitrogen: int
    soil_moisture: float


@app.post("/metrics/{metric_id}", status_code=status.HTTP_201_CREATED)
def create_metric(metric_id: int, metric: CropMetric):
    """Creates a new crop metric record."""
    if metric_id in fake_db:
        # Log a warning and return a 400 Bad Request
        logger.warning(f"Attempted to create duplicate metric ID: {metric_id}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Metric already exists"
        )
    
    fake_db[metric_id] = metric.model_dump()
    # Log an info message on success
    logger.info(f"Successfully created metric {metric_id} for region {metric.region}")
    return {"message": "Metric created successfully", "data": fake_db[metric_id]}


@app.get("/metrics/{metric_id}", status_code=status.HTTP_200_OK)
def get_metric(metric_id: int):
    """Retrieves a specific crop metric record by ID."""
    if metric_id not in fake_db:
        # Log an error and return a 404 Not Found
        logger.error(f"Failed retrieval: Metric ID {metric_id} not found.")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Metric not found"
        )
    
    logger.info(f"Retrieved metric ID {metric_id}")
    return fake_db[metric_id]


@app.delete("/metrics/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_metric(metric_id: int):
    """Deletes a crop metric record by ID."""
    if metric_id not in fake_db:
        logger.warning(f"Attempted to delete non-existent metric ID: {metric_id}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Metric not found"
        )
    
    del fake_db[metric_id]
    logger.info(f"Deleted metric ID {metric_id}")
    
    return