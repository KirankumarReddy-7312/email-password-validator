def form():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    domain = "@algonex.co.in"

    email = f_name + l_name + domain
    print("Your mail id is:", email)

    password = input("Enter strong password: ")
    special_chars = ["@", "#", "&", "$"]

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in special_chars for char in password)
    has_digit = any(char.isdigit() for char in password)

    if len(password) > 6:
        if has_upper and has_lower and has_digit and has_special:
            print("Your password is strong")
        else:
            print("Password must contain uppercase, lowercase, digit, and special character (@, #, &, $)")
    else:
        print("Password must be more than 6 characters")

form()
