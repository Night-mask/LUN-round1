
EigenLayer Brevis Co-chain AVS Setup
21BEC1238

Objective

This document outlines the steps completed for setting up the EigenLayer Brevis Co-chain AVS, including registering an EigenLayer Holesky operator, opting into the Brevis Co-Chain AVS, running it as a systemd service, verifying health status, and setting up node-exporter monitoring with Grafana and Mimir.

Features

- Installed EigenLayer CLI
- Registered EigenLayer Holesky operator
- Opted into Brevis Co-Chain AVS
- Configured Brevis binary to run as a systemd service
- Verified health check endpoint
- Set up node-exporter monitoring with Grafana and Mimir

Steps Completed

 1. Install EigenLayer CLI

- Version Installed: 0.10.3
- Command: Verified version using `eigenlayer --version`

 2. Register an EigenLayer Holesky Operator

- Address`0x2Cd5bD858dAf1492BBC17Bf89265e4F060Db07b4`
- Network: Holesky

   - Attempted to register using the command:
     ```bash
     eigenlayer operator register register-config.yaml
     ```
   - Configuration File: `register-config.yaml`
     ```yaml
     operator:
       address: "0x2Cd5bD858dAf1492BBC17Bf89265e4F060Db07b4"
       network: "holesky"
     ```
   - Issue: Encountered `chain ID 0 not supported`. Investigated alternatives and solutions.

3. Opt into Brevis Co-Chain AVS

- Tokens: Obtained Holesky testnet tokens from the faucet.
- Opt-in Process: Followed EigenLayer instructions to opt into Brevis Co-Chain AVS.

 4. Run Brevis Binary as a Systemd Service

- Service File: Created `brevis.service` file

   ```ini
   [Unit]
   Description=Brevis Co-chain Service
   After=network.target

   [Service]
   ExecStart=/path/to/brevis-binary
   Restart=always
   User=your-username
   Group=your-group

   [Install]
   WantedBy=multi-user.target
   ```

- Commands:
   ```bash
   sudo cp brevis.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable brevis
   sudo systemctl start brevis
   ```

### 5. **Verify Health Check Endpoint**

- Command:
   ```bash
   curl http://localhost:port/health
   ```
   - Replaced `localhost` and `port` with the appropriate values.
   - Screenshot: Provided a screenshot of the response.

6. Setup Node Exporter Monitoring with Grafana and Mimir

- Node Exporter: Installed and started Prometheus node exporter
   ```bash
   sudo apt-get install prometheus-node-exporter
   sudo systemctl start prometheus-node-exporter
   ```

- Grafana: Installed and configured Grafana for visualizing node-exporter metrics
   - Installation Guide: [Grafana Installation Guide](https://grafana.com/docs/grafana/latest/installation/)

- Mimir: Configured Mimir for monitoring
   - Documentation: [Mimir Documentation](https://grafana.com/docs/mimir/latest/)

Deliverables

- Holesky Registered Operator Address: `0x2Cd5bD858dAf1492BBC17Bf89265e4F060Db07b4`
- Systemd File: `brevis.service`
-Systemd Logs: Logs from the `systemd` service
- Health Check Screenshot: Screenshot of the `curl` command response from the health check endpoint


Resources

- EigenLayer Documentation: [EigenLayer Docs](https://docs.eigenlayer.com)
- Holesky Network Information: [Holesky Etherscan](https://holesky.etherscan.io)
- Grafana Documentation: [Grafana Docs](https://grafana.com/docs/grafana/latest/)
- Mimir Documentation: [Mimir Docs](https://grafana.com/docs/mimir/latest/)

Troubleshooting

-Chain ID Issues: Consult EigenLayer documentation or support for alternative methods if chain ID problems persist.
-Consult Documentation**: For detailed troubleshooting, check EigenLayer, Holesky, Grafana, and Mimir documentation.
- Support: Reach out to EigenLayer or Holesky support teams if additional assistance is needed.
