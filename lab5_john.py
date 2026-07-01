# John Wayne | Lab 5 | Intro to Python
# Ticket 1
ages = [17, 11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")
# Ticket 2
keep_checking = "yes"
while keep_checking == "yes":
    user_age = int(input("Enter an age: "))
    if user_age >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")
    
    keep_checking = input("Do you want to check another age? (yes/no): ").lower()


# Ticket 3
while True:
    user_input = input("Enter an age or type 'stop': ")
    if user_input.lower() == "stop":
        break
    
    # Safely convert to integer after checking for stop
    age_input = int(user_input)
    if age_input >= 13:
        print("Access granted ✅")
    else:
        print("Too young ❌")

# Ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False

# Testing the function using the list from Ticket 1
for age in ages:
    if can_access(age):
        print(f"{age} — Access granted ✅")
    else:
        print(f"{age} — Too young ❌")

# Ticket 5
signups = [22, 10, 15, 8, 19, 13]

def signup_report(signup_list):
    print("--- StreamPass Signup Report ---")
    approved = 0
    
    for index, age in enumerate(signup_list, start=1):
        if can_access(age):
            print(f"Signup #{index} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{index} | Age {age} — Too young ❌")
            
    print(f"Approved: {approved} out of {len(signup_list)}")

signup_report(signups)
