from flask import Flask
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
FILE = "/data/contador.txt"

# Métrica personalizada
contador_metric = Counter('acessos_total', 'Número total de acessos à rota /')

@app.route("/")
def index():
    contador_metric.inc()
    os.makedirs("/data", exist_ok=True)
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            f.write("1")
        return "Iniciado com contador 1"
    with open(FILE, "r+") as f:
        count = int(f.read())
        count += 1
        f.seek(0)
        f.write(str(count))
        f.truncate()
    return f"Contador atual: {count}"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
