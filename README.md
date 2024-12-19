# api-demo

demo project to ingest data into bigquery table using API.

A containerized API using Python and FastAPI. Code is packed into a Docker image, and then deployed to Cloud Run. Cloud Run runs the container as a fully managed, serverless service that automatically scales, handles networking, and integrates seamlessly with GCP services such as BigQuery. When requests hit the Cloud Run URL, the service executes code inside the running container, which uses a GCP service account’s credentials to insert data into BigQuery.

1. Local Environment:
   Python code → Package with Docker → Test locally.
2. Deployment Pipeline:
   Push image to GCP registry → Deploy image to Cloud Run → Cloud Run provides a URL.
3. Operation:
   Client (like a user or another service) sends POST requests to the Cloud Run endpoint → Cloud Run runs your FastAPI code → Code streams data into BigQuery using the Cloud Run service account credentials → Data is stored for analysis.
