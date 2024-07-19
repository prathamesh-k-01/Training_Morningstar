import re

'''
	Checking data usage: Queries like "How much data have I used?", "What is my data usage?", "Check data usage."
	Paying bills: Queries like "Pay my bill", "I want to pay my bill", "Bill payment."
	Troubleshooting issues: Queries like "My internet is not working", "Fix my connection", "Troubleshoot internet."


2.	Information Extraction:
o	Extract specific information from the queries, such as the account number, date, and amount.
o	Account numbers are sequences of 8-12 digits.
o	Dates are in the format DD/MM/YYYY or MM/DD/YYYY.
o	Amounts are monetary values preceded by a currency symbol like $ or ₹.

'''

def classify_query(query):
    pattern_check = re.compile(r'.*How much\|What is\|Check data\.*')
    res_check = pattern_check.findall(query)
    if not res_check:
        pass
    else:
        print("The query is a check data query")

    pattern_pay = re.compile(r'\.*Pay my bill\|I want to pay my bill\|Bill payment\|bill payemnt\.*')
    res_pay = pattern_pay.findall(query)
    if not res_pay:
        pass

    else:
        print("THIS IS A PAYING Query")
    pattern_issue = re.compile(r'\.*not working\|fix my connection\|Fix my connection\|Troubleshoot internet\.*')
    res_issue = pattern_issue.findall(query)
    if res_issue:
        print("THe query is a issue query")
    else:
        pass
def extract_info(query):
    pattern_acc = re.compile(r'.*(\d{12}).*')
    result_acc = pattern_acc.findall(query)
    if not result_acc:
        pass
    else:
        print(f'account number is {result_acc}')
    
    
    pattern_date = re.compile(r'.*(\d{4}-\d{2}-\d{2}).*')
    result_date = pattern_date.findall(query)
    if not result_date:
        pass
    
    else:
        print(f'The date is {result_date}')


    pattern_amount = re.compile(r'.*[$\|₹](\d+).*')
    result_amount = pattern_amount.findall(query)
    if not result_amount:
        pass
    else:
        print(f"THe amount you have entered is {result_amount}")

extract_info("My account number is 123456789123, THe date is 2024-07-19 today it is a Friday")
extract_info("THe date is 2024-07-19 today it is a Friday ")
extract_info("Mere pass bohot $400 k note hai")

classify_query("mere gharka internet nahi chal rha fix my connection")