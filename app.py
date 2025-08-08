from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest
import random
import os

app = Flask(__name__)

acessos = Counter("acessos_total", "Número total de acessos à rota /")
temperatura = Gauge("temperatura_ambiente", "Temperatura atual simulada")

@app.route("/")
def index():
    acessos.inc()

    # Simular temperatura
    temperatura.set(random.uniform(20.0, 35.0))  # ex: 25.3

    os.makedirs("/data", exist_ok=True)
    caminho = "/data/contador.txt"

    if os.path.exists(caminho):
        with open(caminho, "r") as f:
            contador = int(f.read())
    else:
        contador = 0

    contador += 1

    with open(caminho, "w") as f:
        f.write(str(contador))

    return f"Iniciado com contador {contador}"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}
