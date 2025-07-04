🔍 Port Scanner using Python

This is a simple **TCP Port Scanner** built using Python. It allows you to scan a range of ports on a given IP address or domain name to check which ports are open. This project simulates the reconnaissance phase used in cybersecurity and ethical hacking.

---

## 📌 Features

- Scan ports from 1 to 1024
- Detect open TCP ports
- Fast execution using socket timeout
- Clean command-line interface

---

## 🧑‍💻 How It Works

The program uses the `socket` module to attempt a connection to each port in the specified range. If a connection is successful (`connect_ex()` returns 0), the port is marked as open.

---

## 🚀 How to Run

### 🔧 Requirements
- Python 3.x installed

### 💻 Run the Script
```bash
Scanner.py
