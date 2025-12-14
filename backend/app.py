from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data (pretend this is coming from a DB)
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
    return jsonify(services)


@app.route("/api/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents)


@app.route("/api/incidents", methods=["POST"])
def create_incident():
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
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
