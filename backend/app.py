"""
Backend API for managing services and incidents using Flask.
Provides endpoints for services, incidents, and health checks.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

services = [
    {"id": 1, "name": "Auth Service", "status": "operational"},
    {"id": 2, "name": "Payment Service", "status": "degraded"},
    {"id": 3, "name": "Notification Service", "status": "operational"},
]

incidents = [
    {
        "id": 1,
        "service_id": 2,
        "title": "Payment delays",
        "status": "investigating",
    }
]


@app.route("/api/services", methods=["GET"])
def get_services():
    """
    Retrieve the list of all services.

    Returns:
        Response: JSON array of service objects.
    """
    return jsonify(services)


@app.route("/api/incidents", methods=["GET"])
def get_incidents():
    """
    Retrieve the list of all incidents.

    Returns:
        Response: JSON array of incident objects.
    """
    return jsonify(incidents)


@app.route("/api/incidents", methods=["POST"])
def create_incident():
    """
    Create a new incident and add it to the incidents list.

    Expects JSON with 'service_id' and 'title'.

    Returns:
        Response: JSON object of the newly created incident.
    """
    data = request.json
    new_incident = {
        "id": len(incidents) + 1,
        "service_id": data["service_id"],
        "title": data["title"],
        "status": "investigating",
    }
    incidents.append(new_incident)
    return jsonify(new_incident), 201


@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify API is running.

    Returns:
        Response: JSON object with status.
    """
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
