# # Q1: regex to validate a 10 digit mobile number:

# import re 
# pattern = r'^[0-9]{10}$'
# number = "9876543210"
# if re.match(pattern,number):
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")


# # Q2: extract email id's from string:

# import re
# sentence = "Contact me at test@gmail.com or admin@yahoo.in"
# pattern = re.findall(r'[\w.-]+@[\w.-]+\.\w+', sentence)
# print(pattern)


# # Q3:extract all the numbers from the sting

# import re
# string = "Order123 price45 quantity6"
# pattern = re.findall(r'\d+',string)
# print(pattern)


# # Q4: validate strong password 
# # -at least 8 characters
# # -one uppercase
# # -one lowercase
# # -one digit
# # -one special character

# import re
# password = "Strong@123"
# pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
# if re.match(pattern, password):
#     print("Valid password")
# else:
#     print("Invalid password")


# # Q5: Validate the pan number

# import re
# pan = "ABCDE1234F"
# pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
# if re.match(pattern, pan):
#     print("Valid PAN number")
# else:
#     print("Invalid PAN number")


# # Q6: ipv4 address validation

# import re
# pattern = (r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}' \
#         r'(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
# ip = "192.168.1.1"
# if re.match(pattern, ip):
#     print("Valid IPv4 address")
# else:
#     print("Invalid IPv4 address")
    
    
# # Q7: ipv6 address validation

# import re
# pattern = r'^([0-9a-fA-F]{1,4}:){2,7}[0-9a-fA-F]{1,4}$'
# ip = "2001:db8:85a3:0000:0000:8a2e:0370:7334"
# print("Valid IPv6" if re.match(pattern, ip) else "Invalid IPv6")


# # Q8: Valid hexa decimal

# import re
# pattern = r'^[0-9A-Fa-f]+$'
# value = "1A3F"
# print("Valid Hexadecimal" if re.match(pattern, value) else "Invalid Hexadecimal")

