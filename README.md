# api-demo

demo project to ingest data into bigquery table using API

Summary of Steps

1. Create requirements.txt and add dependencies.
2. Optionally test locally with uvicorn before containerizing.
3. Install Docker.
4. Build the Docker image locally (docker build ...).
5. Test the Docker image locally (docker run ...).
6. Set up gcloud and ensure project and APIs are enabled.
7. Use gcloud builds submit to build and push image to GCR.
8. Deploy to Cloud Run with gcloud run deploy.
9. Test live endpoint.
10. Ensure Cloud Run’s service account has the right BigQuery permissions
11. Check data in BigQuery.
