# Cowrie Threat Detection Lab

Threat Deception, Log Engineering, and Detection Development — A 4-month R&D project to simulate attacker behavior and detect threats using Cowrie Honeypot and Splunk.

---

## Project Timeline

| Month | Focus Area |
|-------|------------|
| Month 1 | Researched SSH attacks, honeypots, and deception techniques |
| Month 2 | Built and tested Cowrie environments and log formats |
| Month 3 | Developed and tested SPL detections and dashboard visualizations |
| Month 4 | Documentation, final project polish, and GitHub deployment |

---

## Architecture Overview

- Cowrie SSH honeypot (simulated log format)
- Filebeat-style configuration (mocked forwarding)
- Splunk SIEM ingestion via HTTP Event Collector
- Python log injector script
- Custom SPL detections and dashboards

---

## MITRE ATT&CK Mapping

| Technique ID | Technique Name | Description |
|--------------|----------------|-------------|
| T1110.001 | Brute Force | SSH login attempts using password guessing |
| T1059.003 | Command-Line Interface | Shell commands like `wget` and `curl` |
| T1105 | Ingress Tool Transfer | File download activity from remote URLs |

---

## Detection Rules

| Rule | Description |
|------|-------------|
| `ssh-brute-force.spl` | Detects repeated failed login attempts |
| `suspicious-downloads.spl` | Detects use of `wget` or `curl` in honeypot sessions |

---

## Lessons Learned

- Honeypots are valuable for understanding real attacker behavior
- Simulated log analysis is effective for blue team practice
- SPL detection writing shares many parallels with coding logic
- Presentation and documentation matter as much as engineering

---

## Splunk Dashboard

Include screenshot of Splunk dashboard visualizing detection data.

---

## Local Testing Instructions

To simulate a live attack log feed and test detection logic:

```bash
python3 inject_logs.py


Make sure:
  Splunk HEC is enabled and listening on port 8088
  Authorization token is correctly set in the script
  Log file cowrie.json exists in the project root

Certifications and Skills Demonstrated
  CompTIA CySA+
  Splunk Fundamentals 1
  MITRE ATT&CK knowledge
  Detection engineering
  Python scripting for log transport
  Use of GitHub for project versioning and documentation
