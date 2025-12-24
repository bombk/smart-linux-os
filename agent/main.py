import time
import logging
import pandas as pd

from monitor import collect
from detector import AnomalyDetector
from decision import decide
from actions import restart_heavy_process

# Logging
logging.basicConfig(
    filename="/opt/smart-os/logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# Initialize detector
detector = AnomalyDetector()

# 🔹 STEP 1: Train from CSV dataset
csv_path = "/opt/smart-os/data/metrics.csv"
df = pd.read_csv(csv_path)

training_data = df[["cpu", "memory", "disk", "processes"]].values
detector.train(training_data)

logging.info("Model trained using CSV dataset")

# 🔹 STEP 2: Live monitoring loop
while True:
    metrics = collect()

    vector = [
        metrics["cpu"],
        metrics["memory"],
        metrics["disk"],
        metrics["processes"]
    ]

    anomaly = detector.detect(vector)
    action = decide(metrics, anomaly)

    logging.info(
        f"Metrics={metrics} | Anomaly={anomaly} | Action={action}"
    )

    if action == "RESTART_HEAVY_PROCESS":
        restart_heavy_process()

    time.sleep(10)
