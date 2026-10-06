#!/usr/bin/env python3
"""
System Name: Automated Network Telemetry & Configuration Scraper
Author: Daniel Mayowa Mobolade
Role: Cloud & Infrastructure Automation Engineer
Description: Connects to mock network infrastructure via SSH, executes interface commands,
             and parses raw telemetry text strings into production-ready JSON payloads.
"""

import re
import json
import logging
from typing import Dict, Any

# Configure structured logging for NOC observability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- MOCK RAW DATA FOR DEMONSTRATION PURPOSES ---
# This simulates the exact raw unstructured CLI output an engineer gets from an SSH terminal command
MOCK_CLI_OUTPUT = """
Router-Core-01# show interfaces transceiver
Interface        Temperature    Voltage    Tx Power    Rx Power
-----------      -----------    -------    --------    --------
TenGigE0/0/0/1   24.5 C         3.28 V     -2.15 dBm   -3.40 dBm
TenGigE0/0/0/2   28.1 C         3.31 V     -1.90 dBm   -42.0 dBm  [ALARM - LOW RX]
TenGigE0/0/0/3   23.0 C         3.25 V     -2.10 dBm   -3.12 dBm
"""

class TelemetryEngine:
    def __init__(self, target_node: str):
        self.target_node = target_node
        # Compiled Regular Expression to match interface names, Tx/Rx optical metrics, and temperatures
        self.telemetry_regex = re.compile(
            r'(?P<interface>TenGigE\S+)\s+'
            r'(?P<temp>[\d.]+)\s*C\s+'
            r'(?P<voltage>[\d.]+)\s*V\s+'
            r'(?P<tx_power>[-\d.]+)\s*dBm\s+'
            r'(?P<rx_power>[-\d.]+)\s*dBm'
        )

    def scrape_node_telemetry(self) -> str:
        """
        Simulates an SSH connection pool execution using Netmiko.
        In a real infrastructure pipeline, this calls ConnectHandler(device_type, ip, username, password).
        """
        logging.info(r"Establishing secure SSHv2 tunnel to network node: %s", self.target_node)
        try:
            # Simulating netmiko's output = net_connect.send_command('show interfaces transceiver')
            raw_buffer = MOCK_CLI_OUTPUT
            logging.info("Successfully fetched raw optical CLI buffer. Initializing RegEx parsing execution loop.")
            return raw_buffer
        except Exception as error:
            logging.error("Critical Connection Timeout: Failed to reach network endpoint gateway. Details: %s", error)
            raise

    def parse_telemetry_data(self, raw_data: str) -> Dict[str, Any]:
        """
        Parses raw text stream metrics into highly structured, schema-compliant dictionary models.
        """
        parsed_metrics = {
            "source_node": self.target_node,
            "status": "Success",
            "interfaces": []
        }

        # Process the raw CLI buffer line by line
        for line in raw_data.strip().split('\n'):
            match = self.telemetry_regex.search(line)
            if match:
                data = match.groupdict()
                
                # SRE Rule: Trigger an operational flag if Rx optical power drops below dangerous thresholds
                rx_val = float(data["rx_power"])
                status_flag = "CRITICAL_ALARM" if rx_val < -30.0 else "OPTIMAL"

                interface_payload = {
                    "interface_id": data["interface"],
                    "metrics": {
                        "temperature_celsius": float(data["temp"]),
                        "voltage_volts": float(data["voltage"]),
                        "tx_power_dbm": float(data["tx_power"]),
                        "rx_power_dbm": rx_val
                    },
                    "link_state": status_flag
                }
                parsed_metrics["interfaces"].append(interface_payload)

        return parsed_metrics

if __name__ == "__main__":
    print("=====================================================================")
    print(" RUNNING: INFRASTRUCTURE TELEMETRY SCRAPER AUTOMATION DEMO ")
    print("=====================================================================\n")
    
    # Initialize the automated pipeline for a mock core router node
    engine = TelemetryEngine(target_node="10.254.0.1_Core_Router")
    
    # 1. Execute simulated network scraping
    raw_cli_stream = engine.scrape_node_telemetry()
    
    # 2. Parse unstructured strings using RegEx
    structured_json_output = engine.parse_telemetry_data(raw_cli_stream)
    
    # 3. Output the structured payload as pretty JSON (Ready for Timeseries Database Ingestion)
    print("\n[NOC Pipeline Result] Highly Structured Telemetry Payload:")
    print(json.dumps(structured_json_output, indent=4))
    
    print("\n=====================================================================")
    print(" DEPLOYMENT FRAMEWORK EXECUTION COMPLETED SUCCESSFULLY ")
    print("=====================================================================")
