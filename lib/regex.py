import re


# Allows letters, apostrophes, spaces, and hyphens in names
name_regex = re.compile(r"^[A-Za-z]+(?:[ '-][A-Za-z]+)*$")

# Regex for matching a valid phone number (example: 123-456-7890 or (123) 456-7890)
phone_regex = re.compile(r"^(\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?\d{4}$")

# Regex for matching a valid email address
email_regex = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
