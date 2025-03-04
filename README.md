# Advanced Network Speed Test – CLI Tool using speedtest-cli

## Overview

This is an advanced command-line tool to test your internet speed using the `speedtest-cli` Python module. It provides detailed network statistics including download speed, upload speed, ping, server location, ISP details, and latency metrics.

## Features

- Measure download and upload speed.
- Get ping latency.
- Select the best server automatically.
- Display server details (name, country, ISP).
- Save results to a log file for analysis.
- Supports JSON output format for integration with other tools.

## Installation

Ensure you have Python installed, then install the `speedtest-cli` package:

```bash
pip install speedtest-cli
```

## Usage

Run the script using the command:

```bash
python speed_test.py
```

### Additional Options

- To save results to a log file:
  ```bash
  python speed_test.py --log
  ```
- To output results in JSON format:
  ```bash
  python speed_test.py --json
  ```

## Example Output

```bash
Server: XYZ Telecom (New York, USA)
ISP: YourISP
Ping: 12.34 ms
Download Speed: 85.67 Mbps
Upload Speed: 45.23 Mbps
```

## Logging Feature

Results can be saved in a `speed_test.log` file for tracking performance over time.

## License

This project is licensed under the MIT License.
