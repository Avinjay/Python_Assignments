import re

# Function checks if the string contains any special character, upper, lower case, and length
def check_password_strength(string):
    # Create regex patterns
    regex_special = re.compile('[!@_!#$%^&*()<>?/\\|}{~:]')
    regex_up = re.compile('[A-Z]')
    regex_lc = re.compile('[a-z]')
    regex_d = re.compile('[0-9]')

    criteria = 0  # Counter for failed criteria
    missing_criteria = []  # List to store the feedback messages for failed rules
    
    # Check string length
    if len(string) < 8:
        criteria += 1
        missing_criteria.append("Password should be at least 8 characters.")
    
    # Check if uppercase letter is present
    if not regex_up.search(string):
        criteria += 1
        missing_criteria.append("Uppercase letter is not present.")
    
    # Check if lowercase letter is present
    if not regex_lc.search(string):
        criteria += 1
        missing_criteria.append("Lowercase letter is not present.")
    
    # Check if a digit is present
    if not regex_d.search(string):
        criteria += 1
        missing_criteria.append("Digit is not present.")
    
    # Check if special character is present
    if not regex_special.search(string):
        criteria += 1
        missing_criteria.append("Special character is not present.")
    
    # Determine the strength based on the number of missing criteria
    if criteria == 0:
        return (True, "Very Strong", "Password meets all criteria.")
    elif criteria == 1:
        return (False, "Strong", f"Password is strong. Missing the following criterion: {missing_criteria[0]}")
    elif criteria == 2:
        return (False, "Moderate", f"Password is moderate. Missing the following criteria: {', '.join(missing_criteria)}")
    elif criteria == 3:
        return (False, "Weak", f"Password is weak. Missing the following criteria: {', '.join(missing_criteria)}")
    elif criteria == 4:
        return (False, "Very Weak", f"Password is very weak. Missing the following criteria: {', '.join(missing_criteria)}")
    else:
        return (False, "Very Weak", f"Password is very weak. Missing all criteria: {', '.join(missing_criteria)}")

string = input("Please Enter Password\nIt should be more than 8 characters in length, should have at least one uppercase, lowercase, digit, and special character.\n")
result, strength, message = check_password_strength(string)

# Output password strength and message
if result:
    print(message)
else:
    print(f"{message} Your password is considered {strength}.")
