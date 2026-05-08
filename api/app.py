from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
import time
from functools import wraps

app = Flask(__name__)

# Métricas
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de requests recibidas",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Duracion de requests en segundos",
    ["method", "endpoint"]
)

ACTIVE_REQUESTS = Gauge(
    "http_requests_active",
    "Requests activas en este momento"
)

def monitor_metrics(endpoint_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ACTIVE_REQUESTS.inc()
            start_time = time.time()
            try:
                response = func(*args, **kwargs)
                return response
            finally:
                duration = time.time() - start_time
                REQUEST_COUNT.labels(method="GET", endpoint=endpoint_name).inc()
                REQUEST_LATENCY.labels(method="GET", endpoint=endpoint_name).observe(duration)
                ACTIVE_REQUESTS.dec()
        return wrapper
    return decorator

@app.route("/")
@monitor_metrics("/")
def home():
    return jsonify({
        "mensaje": "API de monitoreo funcionando correctamente"
    })

@app.route("/api/datos")
@monitor_metrics("/api/datos")
def datos():
    return jsonify({
        "datos": [
            {"id": 1, "nombre": "CPU", "valor": "35%"},
            {"id": 2, "nombre": "Memoria", "valor": "62%"},
            {"id": 3, "nombre": "Disco", "valor": "48%"}
        ]
    })

@app.route("/api/lento")
@monitor_metrics("/api/lento")
def lento():
    time.sleep(3)
    return jsonify({
        "mensaje": "Respuesta lenta simulada correctamente"
    })

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)