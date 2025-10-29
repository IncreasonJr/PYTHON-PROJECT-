def length_check(password):
    return len(password) >= 8

def uppercase_check(password):
    for char in password:
        if char.isupper():
            return True
    return False

def lowercase_check(password):
    for char in password:
        if char.islower():
            return True
    return False

def specialcharacter_check(password):
    special_characters = "!@#$%^&*()-+?_=,<>/"
    for char in password:
        if char in special_characters:
            return True
    return False

def check_password_strength(password):
    return {
        "length": length_check(password),
        "uppercase": uppercase_check(password),
        "lowercase": lowercase_check(password),
        "special": specialcharacter_check(password),
    }

def main():
    password = input("Enter a password to check its strength: ").strip()
    results = check_password_strength(password)

    for name, passed in results.items():
        if passed:
            status = "OK"
        else:
            status = "Missing"
        print(f"{name.title():9}: {status}")

    problems = []
    for check_name, passed in results.items():
        if not passed:
            if check_name == "length":
                problems.append("Password is too short — it must be at least 8 characters.")
            elif check_name == "uppercase":
                problems.append("Add at least one uppercase letter (A-Z).")
            elif check_name == "lowercase":
                problems.append("Add at least one lowercase letter (a-z).")
            elif check_name == "special":
                problems.append("Add at least one special character (for example: !@#$%).")

    if not problems:
        print("Password strength: STRONG")
    else:
        print("Password strength: NOT STRONG")
        print("Please fix the following:")
        for p in problems:
            print(f"- {p}")

if __name__ == "__main__":
    main()