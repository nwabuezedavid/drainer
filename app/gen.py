import uuid
import random

def genUdis(data):
    codegentrated = str(uuid.uuid4()).replace('-', "")[:data]
    return codegentrated
def referCode(data):
    codes = str(uuid.uuid4()).replace('-', "")[:data]
    return codes
def acc():
    code =  random.randint(10**12, 10**13 - 1) 
    return code
import random
import string

def generate_swift_code():
    # Bank code: 4 uppercase letters
    bank_code = ''.join(random.choices(string.ascii_uppercase, k=4))
    
    # Country code: 2 uppercase letters
    country_code = ''.join(random.choices(string.ascii_uppercase, k=2))
    
    # Location code: 2 letters/digits
    location_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    
    # Optional branch code: 3 letters/digits (can be empty)
    branch_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) if random.choice([True, False]) else ''
    
    # Construct the SWIFT code
    swift_code = f"{bank_code}{country_code}{location_code}"
    if branch_code:
        swift_code += branch_code
    
    return swift_code

# Example usage
swift_code = generate_swift_code()
print("Generated SWIFT Code:", swift_code)



import random

def get_random_name():
    first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Taylor", "Jordan", "Pat", "Robin", "Dana"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"

# Example usage



def get_random_bank_name():
    cities = ["Chestburg", "Greenhill", "Silverbrook", "Eastvale", "Lakewood", "Westfield", "Northgate", "Cedarview"]
    types = ["National Bank", "Federal Trust", "Savings & Loan", "Investment Bank", "Credit Union", "Bank of Commerce", "Financial Group"]

    city = random.choice(cities)
    bank_type = random.choice(types)
    
    return f"{city} {bank_type}"
 