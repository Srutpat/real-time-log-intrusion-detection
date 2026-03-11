
# Real-Time Log-Based Intrusion Detection System

A Python-based real-time security monitoring tool that analyzes web server logs and detects suspicious activity such as brute-force attacks, admin panel probing, reconnaissance scanning, and server errors.

This project demonstrates the basic principles used in security monitoring systems and log analysis platforms.

---

## Features

- Real-time monitoring of web server logs
- Detection of brute-force login attacks (HTTP 401 responses)
- Detection of admin panel probing attempts (HTTP 403)
- Detection of reconnaissance scanning through repeated 404 requests
- Detection of server errors (HTTP 500)
- Generates real-time alerts for suspicious activity
- Generates a final security report summarizing detected threats

---

## How It Works

The system continuously monitors a log file and processes newly added log entries.

Example workflow:
Log File → Python Log Parser → Threat Detection Rules → Security Alerts


The program tracks suspicious patterns based on HTTP status codes and request paths.

---

## Attack Detection Rules

| Attack Type | Detection Logic |
|--------------|----------------|
| Brute Force Attack | Repeated `401` responses from the same IP |
| Admin Panel Probing | Repeated `403` responses on `/admin` endpoints |
| Reconnaissance Scanning | Multiple `404` requests from the same IP |
| Server Errors | `500` responses indicating possible exploitation attempts |

---

## Installation

Clone the repository:
git clone https://github.com/Srutpat/real-time-log-intrusion-detection.git

Navigate to the project folder:
cd log-intrusion-detection


Run the monitor:
python security_monitor.py

---

## Example Log Format


192.168.1.5 - - [11/Mar/2026:10:12:23] "POST /login HTTP/1.1" 401


Log structure:
IP - - timestamp "METHOD URL HTTP" STATUS_CODE

---

## Example Alerts


⚠ ALERT: Possible brute force attack
IP: 192.168.1.20
Failed attempts: 5

⚠ ALERT: Admin panel probing detected
IP: 192.168.1.45
Attempts: 3


---

## Example Final Report


------ FINAL SECURITY REPORT ------

Total Logs Processed: 25

Brute Force Attempts:
192.168.1.20 | failures: 5

Admin Panel Probing:
192.168.1.45 | attempts: 3

Reconnaissance Scanning:
192.168.1.99 | scans: 4

Most Suspicious IP:
192.168.1.20 | failures: 5


---

## Technologies Used

- Python
- Log Parsing
- Pattern Detection
- Real-Time File Monitoring

---

## Future Improvements

- Email or webhook alerts for detected attacks
- Threat scoring system
- Dashboard visualization of attacks
- Integration with real web server logs

---

## Author

Shraddha Ramchandra Utpat  
B.Tech Information Technology  
Pimpri Chinchwad College of Engineering
