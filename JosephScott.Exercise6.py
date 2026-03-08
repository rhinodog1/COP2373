import re

# Function to validate phone numbers
def validate_phone(phone):
    """
    Validates U.S. phone numbers.
    Acceptable formats: 123-456-7890, (123) 456-7890, 1234567890, 123.456.7890, +1 123-456-7890
    Parameters:
        phone (str): The phone number string to validate
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^(\+1\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))


# Function to validate Social Security numbers
def validate_ssn(ssn):
    """
    Validates U.S. Social Security Numbers.
    Format: XXX-XX-XXXX
    Parameters:
        ssn (str): The SSN string to validate
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


# Function to validate U.S. ZIP codes
def validate_zip(zip_code):
    """
    Validates U.S. ZIP codes.
    Formats: 12345 or 12345-6789
    Parameters:
        zip_code (str): The ZIP code string to validate
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


# Main function to get user input and check validity
def main():
    phone = input("Enter a phone number: ")
    ssn = input("Enter a Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code: ")

    print("\nValidation Results:")
    print(f"Phone number valid? {'Yes' if validate_phone(phone) else 'No'}")
    print(f"Social Security Number valid? {'Yes' if validate_ssn(ssn) else 'No'}")
    print(f"ZIP code valid? {'Yes' if validate_zip(zip_code) else 'No'}")


# Test the functions (optional, for demonstration)
if __name__ == "__main__":
    main()