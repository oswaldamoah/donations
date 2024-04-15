import random

class Profile: # Constructor
    def __init__(self, name, age, occupation, donation, id):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.donation = donation
        self.id = id

        

# 
def create_profile():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    occupation = input("Enter your occupation: ")

    while True: # While loop so that without break (for invalid num input), input can be requested again
       try:
            donation = input("Enter donation amount: $")
            break  # Exit loop on successful conversion
       except ValueError:
            print("Invalid donation amount. Please enter a number.")

    id = f"DON-{random.randint(24001, 24100)}"  # Unique ID for donation
    return Profile(name, age, occupation, donation, id)


# Calculating total donation amount and number of donations 
def calculate_totals(profiles):
    total_donations = 0
    num_donations = 0
    for profile in profiles:
       try:
            donation_amount = float(profile.donation)
            total_donations += donation_amount
       except ValueError:
            print(f"Ignoring invalid donation amount for profile: {profile.name}")
       num_donations += 1
    return total_donations, num_donations

# List for object addresses
profiles = []

""" While loop (actually starts running the code) !!!"""
while True:
    new_profile = create_profile()
    profiles.append(new_profile) # Adds profile object to object list

    user_choice = input("Do you want to add another profile? (y/n): ").lower() # Always be lowercased
    if user_choice == 'n':
        break

total_donations, num_donations = calculate_totals(profiles)


# Printing info for individual profiles after exiting data entry loop
print("Profiles:")
for profile in profiles: #For an object in the list
    print("Name:", profile.name)
    print("Age:", profile.age)
    print("Occupation:", profile.occupation)
    print("Donation:", profile.donation)
    print("Your ID is: ", profile.id)
    print()

# Print total donations and number of donations
print(f"\nTotal Donation: ${total_donations:.2f}")
print(f"Number of Donations: {num_donations}")


# COMPLETED
"""
- Create new profile for donator (Name, Age, Occupation, Donation, Random ID)
- Save profile with OOP
- Create multiple identifiable profiles (random ID should be for Identification)
- Total Donation amount + Number of Donations

"""


# Future of this program
"""
- Get profile by ID (Function)
- Get profile by name (Function)
- Edit Profile Details (Function)
- More interactive session (each input leads you to a function)

# Function to show profile based on id
def show_profile_by_name(id=None, name=None):
    for profile in profiles:
        
        if id is None and name is None:
            raise ValueError("At least one of arg1 or arg2 must be provided.")
    
        if profile.id.lower() == id.lower() or profile.name.lower() == name.lower():
            print("Name:", profile.name)
            print("Age:", profile.age)
            print("Occupation:", profile.occupation)
            print("Donation:", profile.donation)
            print()
            break
        else:


            return
    print("Profile not found for the given name.")
"""

