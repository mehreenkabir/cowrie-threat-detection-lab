# 🕵️ Cowrie Honeypot Detection Architecture (Splunk Edition)

This project simulates a real-world SSH honeypot detection pipeline using [Cowrie](https://github.com/cowrie/cowrie), Splunk, and custom SPL rules — built to detect, analyze, and visualize attacker behavior.

---

## 🎯 Why I Built This

As a security analyst and engineer, I wanted to create a fun and functional way to show hands-on skills in:
- Threat detection
- Log ingestion
- SPL detection writing
- Honeypot deception techniques
- Real-world threat emulation

I also wanted to feel like an **ethical hacker catching bad guys** — so I made a trap, watched it get hit, and wrote detections for it 😈

---

## ⚙️ Architecture Overview

- 🐍 **Cowrie** Honeypot (Simulated via `cowrie.json`)
- 📤 **Filebeat** Config (Simulated forwarder)
- 🔍 **Splunk** (Local instance)
- 📊 **Custom Detections** in SPL

---

## 🔐 Detections

| Detection | Description |
|----------|-------------|
| [`ssh-brute-force.spl`](detections/ssh-brute-force.spl) | Detects repeated failed login attempts from the same IP |
| [`suspicious-downloads.spl`](detections/suspicious-downloads.spl) | Detects use of wget or curl in honeypot sessions |

---

## 🛠 How I Simulated the Logs

I created fake attacker logs using a TryHackMe Kali Linux box and local tools. The logs are available in [`cowrie.json`](cowrie.json).

Then I tested log ingestion using Splunk’s HEC:

```bash
curl -k http://localhost:8088/services/collector \
  -H "Authorization: Splunk <your-token>" \
  -H "Content-Type: application/json" \
  -d '{"sourcetype": "cowrie", "event": {"eventid":"cowrie.login.failed","username":"root","src_ip":"111.111.111.111"}}'
