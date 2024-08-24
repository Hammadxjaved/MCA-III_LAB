import secrets

def generate_otp():
    return secrets.randbelow(900000) + 100000

print("Secure OTP:", generate_otp())
