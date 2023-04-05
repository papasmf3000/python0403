import re

ssn_pattern = r"\d{6}-\d{7}"
ssn = "800101-1079512"

if re.search(ssn_pattern, ssn):
    print("Valid SSN")
else:
    print("Invalid SSN")
