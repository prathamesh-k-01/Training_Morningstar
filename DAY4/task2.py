import re 
from task1 import log_data
#Task 2: Counting Different Log Levels
#Write a Python function to count the number of occurrences of each log level (ERROR, INFO, WARNING).

pattern = re.compile(r'\[(ERROR|INFO|WARNING)\]')
matches = pattern.findall(log_data)
result =  {level: matches.count(level) for level in set(matches)}
print(result)
