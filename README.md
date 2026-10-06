# Automated Network Telemetry & Configuration Scraper

An asynchronous, production-grade automation engine designed to establish secure SSH connections to enterprise network infrastructure, execute telemetry commands, parse raw unstructured CLI outputs using advanced Regular Expressions (RegEx), and prepare data structures for database ingestion.

## 🏗️ System Architecture

+--------------------+             +-----------------------------+
|  Enterprise Core   |  (SSH/v2)   |  Python Automation Engine   |
|  Switches/Routers  | ------------> |  - Netmiko Connection Pool  |
|  (Cisco,  Huawei)  |             |  - RegEx Tokenizer Engine   |
+--------------------+             +-----------------------------+
|
v
+--------------------+             +-----------------------------+
| Unified Observability| <---------- |  Structured JSON Output     |
| Dashboard / DB Layer|            |  (Telemetry Database)       |
+--------------------+             +-----------------------------+

## 🚀 Core Features
- **Secure Remote Orchestration:** Multi-node connection handling leveraging SSHv2 via `Netmiko`.
- **Deterministic Tokenization:** Granular `RegEx` compilation to extract link states, optical power levels (dBm), temperature thresholds, and baseline configurations.
- **Fail-Safe Exception Handling:** Built-in catch blocks for authentication failures, protocol timeouts, and unreachable network gateways to protect NOC integrity.
- **Platform Agnostic Data Modeling:** Transforms raw CLI string buffers into standardized JSON maps ready for timeseries databases or custom UI dashboards.

## 🛠️ Tech Stack & Requirements
- **Language:** Python 3.10+
- **Core Frameworks:** `netmiko`, `re` (Standard Regex Library)

To initialize the environment locally:
```bash
pip install netmiko
```

## 💻 Sample Execution
Run the core daemon wrapper to simulate infrastructure scraping:
```bash
python telemetry_scraper.py
