import re

def is_valid_korean_ssn(ssn):
    pattern = r'^[0-9]{6}\-[0-9]{7}$'
    return bool(re.match(pattern, ssn))

# example usage
ssn = '800101-1079515'
if is_valid_korean_ssn(ssn):
    print(f"{ssn} is a valid Korean social security number")
else:
    print(f"{ssn} is not a valid Korean social security number")
