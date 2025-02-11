# Python Assignments

## Overview
This repository contains various Python scripts developed as part of DevOps certification assignments. Each script serves a different purpose, including configuration management, database interaction, system monitoring, and security checks.

## Project Structure

- **Confpar.py**: Reads configuration files and inserts the configuration into MongoDB.
-- **Configuration.txt**: Stores Input Configuration files
- **Configuration_mongo.txt**: Stores MongoDB URI for database connections.
- **CPU.py**: Monitors CPU usage and alerts if the threshold is exceeded.
- **Sp.py**: Checks password strength based on multiple security criteria.

## Setup Instructions

### Prerequisites
Ensure you have Python installed (>=3.6) and install required dependencies:

```sh
pip install -r requirements.txt
```

### Running the Scripts
- **Configuration Management**
  - Modify `Configuration.txt` and `Configuration_mongo.txt` as needed.
  - Run `python Confpar.py` to insert configuration data into MongoDB.

- **CPU Monitoring**
  - Run `python CPU.py` to start CPU monitoring.
  
- **Password Strength Checker**
  - Run `python Sp.py` and enter a password to check its strength.

## Dependencies
Refer to `requirements.txt` for all required Python libraries.

