# Raspberry Pi 5 System Dashboard

A lightweight, web-based dashboard to monitor CPU usage, RAM usage, disk usage, temperature, uptime, power consumption, and top CPU-consuming processes on a Raspberry Pi 5.  
Built with Python Flask backend and a responsive frontend using Chart.js for visualization.

---

## Features

- Real-time monitoring of:
  - CPU usage (%)
  - RAM usage (GB and %)
  - Disk usage (GB and %)
  - CPU temperature (°C)
  - System uptime (human-readable)
  - Estimated power consumption (Watts and kWh)
- Display of top 5 CPU-consuming processes
- Combined line chart showing CPU, RAM, Disk, and Temperature over time
- Responsive design with light/dark mode based on user system preference
- Accessible from any device on your local network

---

## Requirements

- Raspberry Pi 5 (or compatible Linux system)
- Python 3.7+
- Python packages:
  - Flask
  - psutil

---

## Installation & Setup

Install required Python packages:

pip install Flask psutil
Run the Flask app:

python app.py

Open a browser on any device on the same LAN and navigate to:

http://<Raspberry_Pi_IP>:5000
