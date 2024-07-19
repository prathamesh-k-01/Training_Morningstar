#Task 1: Extracting All Timestamps
#Write a Python function to extract all timestamps from the log file.

import re

log_data = """
[2024-07-18 10:23:45] [ERROR] [Authentication] User login failed
[2024-07-18 10:24:00] [INFO] [Payment] Payment processed successfully
[2024-07-18 10:25:30] [WARNING] [Database] Connection timeout
[2024-07-18 10:27:15] [INFO] [Authentication] User login succeeded
"""

pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]')

print(pattern.findall(log_data))