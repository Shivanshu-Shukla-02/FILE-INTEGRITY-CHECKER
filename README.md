# FILE-INTEGRITY-CHECKER

**COMPANY NAME**: CODTECH IT SOLUTIONS 

**NAME**:  SHIVANSHU SHUKLA

**INTERN ID**: CT08NFT

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: January 15th, 2025 to February 15th, 2025

**MENTOR NAME**: Neela Santhosh Kumar

# ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS


The task involved designing and implementing a Python-based tool to monitor file changes by calculating and comparing cryptographic hash values. This tool is essential for ensuring file integrity, detecting unauthorized modifications, and maintaining security in file systems. Using Python's hashlib library as the core for hash generation, the script systematically tracks files in a specified directory, logging any detected changes.

Task Goals
Ensure File Integrity:
By comparing hash values over time, the tool provides a mechanism to verify whether files have been altered, added, or deleted.
Automated Monitoring:
The script automates the process of file scanning, eliminating the need for manual checks.
Real-Time Alerts:
Provide immediate notifications for changes, ensuring rapid responses to unauthorized activities.
Steps Taken to Develop the Tool
1. Requirements Analysis:
The first step was identifying the requirements for the tool:

It should compute hash values for each file in a directory.
Allow users to specify directories for monitoring.
Detect and classify changes into modified, added, or deleted files.
Provide clear logs or reports of detected changes.
2. Selection of Tools and Libraries:
Python was chosen for its versatility and rich library ecosystem. The primary libraries used were:

hashlib: For generating cryptographic hash values such as SHA-256.
os and os.path: For directory traversal and file operations.
pickle or json: For storing and retrieving hash data persistently.
3. Tool Design and Architecture:
The script was structured to be modular, with the following core functionalities:

Hash Generation: Using hashlib, the tool generates hash values for files. SHA-256 was chosen for its strong collision resistance.
Data Persistence: The tool saves hash values to a local file (e.g., hash_data.json) for later comparison.
Change Detection: By comparing the current hashes with stored values, the script categorizes changes into:
Modified Files: Files with differing hash values.
Added Files: New files not present in the stored hash data.
Deleted Files: Files missing from the directory but present in the stored data.
Logging and Reporting: Changes are logged to the console and optionally saved to a report file.
4. Implementation:
The script was implemented in Python. Below are the key steps performed in the implementation:

Recursive Directory Scanning:
The tool traverses the directory tree using os.walk(), ensuring all files, including those in subdirectories, are monitored.
Hash Calculation:
A hash value is computed for each file by reading it in binary mode and feeding its content to the hashlib.sha256() function.
Data Storage:
The hash values, along with file paths, are stored in a JSON file for future reference.
Change Detection Logic:
On subsequent runs, the script compares the newly calculated hashes against the stored ones, detecting any changes and updating the hash file accordingly.
User Interaction:
The tool offers a simple command-line interface (CLI) for specifying the directory and running the monitoring process.
5. Testing:
The tool was tested extensively to ensure reliability. Different scenarios were simulated:

Modifying a file's content.
Adding new files to the directory.
Deleting existing files. Each test successfully detected the changes and generated the appropriate logs.
6. Enhancements:
After basic functionality was achieved, the following enhancements were added:

Real-Time Monitoring: Implemented periodic checks using time.sleep() for real-time file tracking.
Customizable Algorithms: Allowed users to select between hash algorithms (e.g., MD5, SHA-1, SHA-256).
Output Options: Users could choose to log results to a file or the console.

**OUTOUT**: 
$ python file_monitor.py
Enter the directory to monitor: ./monitor_directory
Monitoring changes in: ./monitor_directory
Press Ctrl+C to stop.
(No changes detected)



