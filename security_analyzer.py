import time

failed_ip = {}
admin_access = {}
server_errors = {}
scan_attempts = {}

last_position = 0
total_logs = 0


def detect_threat(ip, url, status):

    if status == "401":
        failed_ip[ip] = failed_ip.get(ip, 0) + 1

        if failed_ip[ip] >= 5:
            print("\n⚠ ALERT: Possible brute force attack")
            print("IP:", ip)
            print("Failed attempts:", failed_ip[ip])

    if "admin" in url and status == "403":
        admin_access[ip] = admin_access.get(ip, 0) + 1

        if admin_access[ip] >= 3:
            print("\n⚠ ALERT: Admin panel probing detected")
            print("IP:", ip)
            print("Attempts:", admin_access[ip])

    if status == "500":
        server_errors[ip] = server_errors.get(ip, 0) + 1

        print("\n⚠ ALERT: Server error triggered")
        print("IP:", ip)

    if status == "404":
        scan_attempts[ip] = scan_attempts.get(ip, 0) + 1

        if scan_attempts[ip] >= 4:
            print("\n⚠ ALERT: Possible reconnaissance scanning")
            print("IP:", ip)
            print("404 requests:", scan_attempts[ip])


def print_report():

    print("\n\n------ FINAL SECURITY REPORT ------")

    print("\nTotal Logs Processed:", total_logs)

    print("\nBrute Force Attempts:")
    for ip, count in failed_ip.items():
        if count >= 3:
            print(ip, "| failures:", count)

    print("\nAdmin Panel Probing:")
    for ip, count in admin_access.items():
        if count >= 3:
            print(ip, "| attempts:", count)

    print("\nServer Errors:")
    for ip, count in server_errors.items():
        print(ip, "| errors:", count)

    print("\nReconnaissance Scanning:")
    for ip, count in scan_attempts.items():
        if count >= 4:
            print(ip, "| scans:", count)

    if failed_ip:
        suspicious = max(failed_ip, key=failed_ip.get)
        print("\nMost Suspicious IP:", suspicious,
              "| failures:", failed_ip[suspicious])


print("Monitoring logs for threats...\n")

try:

    while True:

        with open("access.log", "r") as file:

            file.seek(last_position)

            lines = file.readlines()

            last_position = file.tell()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            if len(parts) < 7:
                continue

            ip = parts[0]
            url = parts[6]
            status = parts[-1]

            total_logs += 1

            detect_threat(ip, url, status)

        time.sleep(1)

except KeyboardInterrupt:

    print("\nStopping monitor... generating report...")

finally:

    print_report()