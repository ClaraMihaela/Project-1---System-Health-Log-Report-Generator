# System Health & Log Report Generator

A lightweight Python automation tool that parses application log files, 
categorizes system events (`INFO`, `WARNING`, `ERROR`), and automatically generates a 
structured daily health report to speed up manual log review.

# Features
- Automated Log Parsing: Reads system log files line by line and filters critical entries.
- Event Categorization: Counts `INFO`, `WARNING`, and `ERROR` occurrences for a better stability.
- Dynamic Health Status: Determines overall system status (`HEALTHY`, `WARNING`, or `CRITICAL`) based on detected issues.
- Structured Reporting: Outputs a clean summary report (`daily_report.txt`).

# Project Structure
log_report_generator.py   # Main Python script
system_logs.txt           # Sample input log file
daily_report.txt          # Generated output report
README.md                 # Project documentation