import re

phone_pattern = r"\d{3}-\d{3,4}-\d{4}"
phone_number = "010-1234-5678"

if re.search(phone_pattern, phone_number):
    print("Valid phone number")
else:
    print("Invalid phone number")
