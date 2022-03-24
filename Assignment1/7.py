import re

password = input()

if (re.search(r'[a-z]',password) and re.search(r'[A-Z]',password) and re.search(r'[0-9]',password) and re.search(r'[\@\#\$]',password) and len(password) >= 6 and len(password) <= 16):
    print("Valid")
else:
    print("Invalid")