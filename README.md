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

## Run the Flask app:

python app.py

## Open a browser on any device on the same LAN and navigate to:

http://<Raspberry_Pi_IP>:5000

## File Structure
app.py — Flask backend server collecting system stats and serving API endpoints

templates/index.html — Frontend dashboard page with dynamic updates and chart

static/ — (optional) for CSS, JS assets if you choose to separate

## License Information
Flask — BSD-3-Clause License

psutil — BSD License

Chart.js — MIT License

This project code — [Your choice; e.g., MIT License]

## Notes
The power consumption estimation assumes a Raspberry Pi 5 with a 5V 5A power supply (27W max). Real usage may vary.

For production use, consider running Flask behind a WSGI server like Gunicorn and optionally enable HTTPS for security.

Make sure to open port 5000 on your Raspberry Pi firewall if accessing from other devices.

## Contact
For questions or contributions, please open an issue or submit a pull request.
