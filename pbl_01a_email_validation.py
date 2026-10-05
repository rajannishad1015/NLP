import re

pattern = r"\b[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = input("Enter the email: ")
match = re.match(pattern, email)
if match:
    print(match.group(), "it is valid")
else:
    print("No match found")
