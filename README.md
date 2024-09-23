# Server Automation for RDS Instances

This repository contains scripts to automate the start and stop operations for AWS RDS instances using AWS Lambda and Python (with `boto3`). The scripts `rds_start.py` and `rds_stop.py` are designed to be used within an AWS Lambda environment.

## Files in This Repository

###  `rds_start.py`
- **Purpose**: This script is used to start AWS RDS instances automatically.
- **How It Works**:
  - Retrieves the list of RDS instances from the Lambda environment variable `RDS_instances`.
  - Iterates over each instance and starts it using the `boto3` library.
- **Usage**:
  - This script is designed to run in an AWS Lambda environment. Ensure that the environment variable `RDS_instances` contains a comma-separated list of RDS instance identifiers.

###  `rds_stop.py`
- **Purpose**: This script is used to stop AWS RDS instances automatically.
- **How It Works**:
  - Retrieves the list of RDS instances from the Lambda environment variable `RDS_instances`.
  - Iterates over each instance and stops it using the `boto3` library.
- **Usage**:
  - Like `rds_start.py`, this script is designed to run in an AWS Lambda environment with the `RDS_instances` environment variable properly configured.
