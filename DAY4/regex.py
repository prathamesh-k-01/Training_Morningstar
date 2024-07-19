import re

# pattern = re.compile(r'hello', re.IGNORECASE)

# # result = pattern.search("HELLO world")

# # print(result.group())


# # pattern = re.compile(r'hello.world', re.DOTALL)
# result = pattern.search('hello\nworld')

# print(result.group())


# match vs search

result = re.match(r'\d+', '123 def')
print(result.group())

result = re.match(r'\d+', 'abc 123 def')
print(result)