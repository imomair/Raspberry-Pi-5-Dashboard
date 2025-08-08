from flask import Flask, render_template, jsonify
import psutil
import subprocess
import platform
import time

app = Flask(__name__)

POWER_SUPPLY_VOLTAGE = 5.0  # Volts
POWER_SUPPLY_CURRENT = 5.0  # Amps
POWER_SUPPLY_WATTAGE = POWER_SUPPLY_VOLTAGE * POWER_SUPPLY_CURRENT  # Watts

def get_temperature():
    # Try vcgencmd (Pi 4, 3). On Pi 5 may fail, fallback to psutil or N/A
    try:
        out = subprocess.check_output(["vcgencmd", "measure_temp"]).decode().strip()
        return out.replace("temp=", "")
    except Exception:
        try:
            temps = psutil.sensors_temperatures()
            if temps:
                for entries in temps.values():
                    if entries:
                        return f"{entries[0].current:.1f}°C"
        except Exception:
            pass
    return "N/A"

def format_uptime(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    return f"{days}d {hours}h {minutes}m"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    cpu = psutil.cpu_percent(interval=0.1)
    virtual_mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime_seconds = int(time.time() - psutil.boot_time())
    temperature = get_temperature()
    hostname = platform.node()

    # Calculate power consumption in kWh since boot (Watt * hours / 1000)
    hours_on = uptime_seconds / 3600
    kwh_used = round((POWER_SUPPLY_WATTAGE * hours_on) / 1000, 3)

    return jsonify({
        "timestamp": int(time.time() * 1000),
        "cpu_percent": cpu,
        "ram_used_gb": round(virtual_mem.used / (1024**3), 2),
        "ram_total_gb": round(virtual_mem.total / (1024**3), 2),
        "ram_percent": virtual_mem.percent,
        "disk_used_gb": round(disk.used / (1024**3), 2),
        "disk_total_gb": round(disk.total / (1024**3), 2),
        "disk_percent": disk.percent,
        "temperature": temperature,
        "hostname": hostname,
        "uptime_seconds": uptime_seconds,
        "uptime_str": format_uptime(uptime_seconds),
        "power_watts": POWER_SUPPLY_WATTAGE,
        "kwh_used": kwh_used
    })

@app.route("/api/topprocs")
def topprocs():
    procs = []
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        procs.append(p.info)
    procs.sort(key=lambda x: x['cpu_percent'], reverse=True)
    return jsonify(procs[:5])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
