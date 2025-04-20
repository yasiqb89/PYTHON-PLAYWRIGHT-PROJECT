

valid_credentials = {
    "username": "standard_user",
    "password": "secret_sauce"
}


invalid_credentials = [
    {"username": "", "password": "", "error": "Epic sadface: Username is required"},
    {"username": "standard_user", "password": "", "error": "Epic sadface: Password is required"},
    {"username": "invalid_user", "password": "wrong", "error": "Epic sadface: Username and password do not match any user in this service"},
    {"username": "😈" * 1000, "password": "!@#$%^&*()_+{}|:<>?~`" * 20, "error": "Epic sadface: Username and password do not match any user in this service"}
]


locked_out_user = [
    {"username": "locked_out_user", "password": "secret_sauce", "error": "Epic sadface: Sorry, this user has been locked out."}
]
