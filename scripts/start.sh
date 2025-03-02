#!/bin/bash

# Start the FastAPI application with Uvicorn
# --reload: Enable auto-reload on code changes
# --host: Listen on all network interfaces
# --port: Use port 8000
uvicorn main:app --reload --host 0.0.0.0 --port 8000