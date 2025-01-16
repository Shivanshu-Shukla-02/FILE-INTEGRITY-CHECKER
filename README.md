# FILE-INTEGRITY-CHECKER

**COMPANY NAME**: CODTECH IT SOLUTIONS 

**NAME**:  SHIVANSHU SHUKLA

**INTERN ID**: CT08NFT

**DOMAIN**: CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION**: January 15th, 2025 to February 15th, 2025

**MENTOR NAME**: Neela Santhosh Kumar

# ENTER DESCRIPTION OF TASK PERFORMED NOT LESS THAN 500 WORDS


The assignment required creating and deploying a Python-based tool that could track file modifications by calculating and comparing cryptographic hash values. This tool is crucial for guaranteeing file integrity, identifying unauthorized changes, and upholding security in file systems. By utilizing python's hashlib library as the foundation for hash generation, the script systematically monitors files within a designated directory, recording any detected alterations.

Task goals guarantee file integrity: by comparing hash values over time, the tool offers a way to verify if files have been modified, added, or removed. Automated monitoring: the script automates the process of file scanning, eliminating the need for manual checks. Real-time alerts: offer instant notifications for alterations, guaranteeing swift responses to unauthorized actions. The process of creating the tool involved several steps.

The assignment required creating and deploying a Python-based tool that could track file modifications by calculating and comparing cryptographic hash values. This tool is crucial for guaranteeing file integrity, identifying unauthorized changes, and upholding security in file systems. By utilizing python's hashlib library as the foundation for hash generation, the script systematically monitors files within a designated directory, recording any detected alterations.

Task goals guarantee file integrity: by comparing hash values over time, the tool offers a way to verify if files have been modified, added, or removed. Automated monitoring: the script automates the process of file scanning, eliminating the need for manual checks. Real-time alerts: offer instant notifications for alterations, guaranteeing swift responses to unauthorized actions. The process of creating the tool involved several steps.

4: Implementation:: The code was written in Python.
The following are the essential steps involved in the execution of the plan: Recursive directory scanning: The tool navigates the directory structure using os. Walk(), guaranteeing that all files, including those in subdirectories, are monitored.
Hash calculation:
The hash value for each file is determined by reading it in binary mode and passing its content to the hashlib. Sha256() function.
Data retention:
The hash values, in addition to file paths, are saved in a JSON file for future use.
Change detection logic:
In subsequent runs, the script compares the newly calculated hashes with the stored ones, identifying any modifications and updating the hash file accordingly.
User engagement:
The tool provides a straightforward command-line interface (cli) that allows users to specify the directory and initiate the monitoring process.

5: Testing::
The tool underwent rigorous testing to guarantee its dependability.
Various situations were modeled: Editing a document's data.
Incorporating fresh files into the directory.
Removing previously created files. Each test accurately identified the alterations and produced the necessary logs.


6: Enhancements:: Once the basic functionality was established, the following enhancements were implemented: Real-time monitoring: implemented periodic checks using time. Sleep() for real-time file tracking.
Customizable algorithms: enabled users to choose from a variety of hash algorithms, such as md5, sha-1, and sha-256.
Users had the option to either save the results to a file or display them in the console.


**OUTOUT**: 
$ python file_monitor.py
Enter the directory to monitor: ./monitor_directory
Monitoring changes in: ./monitor_directory
Press Ctrl+C to stop.
(No changes detected)



