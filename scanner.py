import socket
import requests

def port_scan(target, ports):
    print(f"Starting port scan on {target}")
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"Port {port} is open.")
    return open_ports

def vulnerability_scan(url):
    print(f"Starting vulnerability scan on {url}")
    vulnerabilities = []
    # Check for standard directories (example vulnerability check)
    directories = ['admin', 'login', 'config', 'backup']
    for dir in directories:
        full_url = f"{url}/{dir}"
        response = requests.get(full_url)
        if response.status_code == 200:
            vulnerabilities.append(f"Potentially sensitive directory found: {full_url}")
            print(f"Vulnerability found at {full_url}")

    # Example version check vulnerability
    response = requests.get(url)
    server_header = response.headers.get("Server", "")
    if "Apache" in server_header:
        vulnerabilities.append("Potentially vulnerable Apache server detected.")
        print("Vulnerable Apache server version detected.")
    return vulnerabilities

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    ports_to_scan = [21, 22, 80, 443, 8080]  # Standard ports for demo
    open_ports = port_scan(target_ip, ports_to_scan)

    target_url = input("Enter target URL (e.g., http://example.com): ")
    found_vulnerabilities = vulnerability_scan(target_url)

    print("\nScan Results:\n")
    print("Open Ports:", open_ports)
    print("Vulnerabilities:", found_vulnerabilities)
