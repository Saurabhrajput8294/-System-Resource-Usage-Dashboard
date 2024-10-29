# System Resource Usage Dashboard

A **Text User Interface (TUI) dashboard** built with Python that displays real-time system statistics such as **CPU, memory, disk, and network usage**. This project uses the `curses` library for TUI rendering and `psutil` for system resource monitoring.

## Features
- **Real-time monitoring** of:
  - CPU usage
  - Memory usage (Total, Used, Free)
  - Disk usage (Total, Used, Free)
  - Network statistics (Bytes Sent and Received)
- **Save reports** to a text file on demand.
- Simple key-based controls:
  - Press `q` to quit.
  - Press `s` to save the current report.

## Prerequisites
Ensure the following are installed on your system:
- **Python 3.x**
- **pip** (Python package manager)
- **psutil** library for system resource monitoring

### Install Dependencies
Use the following command to install `psutil`:
```bash
pip3 install psutil
