email_address = input("Enter Your Email: ").strip()
user_name = email_address[:email_address.index("@")]
domain_name = email_address[email_address.index("@")+1:]
format = (f"Your user name is '{user_name}' and your domain is '{domain_name}'")
print(format)