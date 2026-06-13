from datetime import datetime, timezone
from flask import Flask, jsonify
from flask_cors import CORS

from config import Config


app = Flask(__name__)
CORS(app)


@app.get("/health")
def health_check():
    """
    Lightweight health endpoint.

    Kubernetes will later use this endpoint for liveness/readiness probes.
    Docker Compose can also use it for local container health checks.
    """
    return jsonify({
        "status": "healthy",
        "service": Config.APP_NAME,
        "version": Config.APP_VERSION
    })


@app.get("/api/system-info")
def get_system_info():
    """
    Returns runtime information about the current backend instance.

    In Kubernetes, when multiple replicas are running, the podName value
    helps us see which Pod handled the request.
    """
    return jsonify({
        "service": Config.APP_NAME,
        "version": Config.APP_VERSION,
        "environment": Config.APP_ENV,
        "podName": Config.POD_NAME,
        "serverTimeUtc": datetime.now(timezone.utc).isoformat(),
        "status": "healthy",
        "secretConfigured": bool(Config.DEMO_API_KEY),
        "databaseReady": Config.is_database_configured()
    })


@app.get("/api/orders")
def get_orders():
    """
    Demo business endpoint.

    For now, this returns static data. Later, this endpoint can be changed
    to read from a real database without changing the frontend contract.
    """
    return jsonify({
        "items": [
            {
                "id": 1,
                "customer": "Demo Customer",
                "service": "Premium Wash",
                "status": "scheduled"
            },
            {
                "id": 2,
                "customer": "Test Client",
                "service": "Exterior Wash",
                "status": "completed"
            }
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)