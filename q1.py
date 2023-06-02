import re

def validate_password(password):
    pattern = r"(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d]{8,}"
    match = re.match(pattern, password)
    if match:
        return True
    else:
        return False