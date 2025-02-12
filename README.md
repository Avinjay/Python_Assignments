# Python Assignments

This repository contains Python scripts developed as part of a DevOps certification. The assignments cover various functionalities, including configuration file parsing, MongoDB integration, system monitoring, and password strength validation.

---

## **Project Structure**
- `Configuration.txt` - Stores database and server configurations.
- `Configuration_mongo.txt` - Stores MongoDB connection URI.
- `Confpar.py` - Parses configuration files and inserts data into MongoDB.
- `CPU.py` - Monitors CPU usage and triggers alerts when usage exceeds a set threshold.
- `Sp.py` - Checks password strength based on predefined security criteria.

---

## **Installation**

1. **Install Python**

      Ensure Python is installed on your system (Python 3.6 or higher is recommended).
   - Download and install from the official [Python website](https://www.python.org/downloads/).
   - Verify installation by running:
     ```sh
     python --version
     ```

2. **Clone the repository**
   
   git clone git@github.com:Avinjay/Python_Assignments.git
   
   cd Python_Assignments

 **Install dependencies**
 
pip install -r requirements.txt

## **Usage**
1. Configuration Parser (Confpar.py)
INI File and ConfigParser:
INI files are plain-text configuration files consisting of sections, each containing key-value pairs. The Python configparser module provides a ConfigParser class to read and parse INI files.

2. Constructor and Nested Dictionary Usage:
The script uses the ConfigParser() constructor to create a parser object. The parsed data is converted to a nested dictionary structure where each section in the INI file is represented as a dictionary of key-value pairs. This allows easy manipulation of the configuration as a Python object.

python Confpar.py

This script reads the configuration from Configuration.txt, inserts the data into MongoDB, and fetches the stored data for display.

Input File

![image](https://github.com/user-attachments/assets/f7dcc9c2-13ae-472d-a2e7-08ff8713c506)

Output

![image](https://github.com/user-attachments/assets/51389703-940e-4fc4-a333-fa5e3b339aed)

2. CPU Monitoring (CPU.py)
psutil Module:
psutil (Python System and Process Utilities) is a cross-platform library for retrieving information on system utilization, such as CPU, memory, disk, and network usage. The cpu_percent(interval=1) method is used to monitor CPU usage at 1-second intervals.

python CPU.py

The script continuously monitors CPU usage and raises an alert if the usage exceeds a defined threshold (15% in this case).

The program takes threshold from user & throws alert when CPU breaches that threshold, it also throws keyboard interruption error
![image](https://github.com/user-attachments/assets/295f2229-e0ba-4147-9d21-7965b7d1e1a7)

3. Password Strength Checker (Sp.py)

re Module:
The re (regular expression) module is used for pattern matching in strings. The script uses the compile method to precompile regular expressions for uppercase letters, lowercase letters, digits, and special characters to improve performance. The search method checks whether the provided password contains characters that match the specified patterns.


python Sp.py

Length, Digit & Special Chararacter Validation

![image](https://github.com/user-attachments/assets/d654a6de-5c99-4ead-bd88-a264166c2e90)

Digit Validation
![image](https://github.com/user-attachments/assets/7a01c8dd-9c8a-4d39-b374-38ffadc4791e)

Success Pattern

![image](https://github.com/user-attachments/assets/3a4b676b-1181-45a1-bc36-67a7e48cefc7)




