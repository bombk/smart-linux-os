import psutil
import logging

def restart_heavy_process():
    for p in psutil.process_iter(['pid', 'cpu_percent', 'name']):
        try:
            if p.info['cpu_percent'] and p.info['cpu_percent'] > 20:
                logging.warning(f"Killing process {p.info['name']} (PID {p.pid})")
                p.terminate()
                break
        except Exception:
            pass
