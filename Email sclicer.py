#email sclicer

email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:] #+1 is used cause we don't want @ in output

print(f"Your username is {username} & domain is {domain}")
# f is used to create an f-string (formatted string literal).
