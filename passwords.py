import hashlib

# Hashing function using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Stored login credentials: email -> hashed password
stored_logins = {
    "alice@example.com": hash_password("apple123"),
    "bob@example.com": hash_password("banana456"),
    "carol@example.com": hash_password("cherry789")
}

# Login function to verify user
def login(email, password_to_check):
    # Hash the entered password
    hashed_password = hash_password(password_to_check)
    
    # Check if email exists and hashed password matches
    return stored_logins.get(email) == hashed_password

# Example usage
print(login("alice@example.com", "apple123"))  # True
print(login("bob@example.com", "wrongpass"))   # False
