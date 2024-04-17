import random

class Profile: # Constructor
    def __init__(self, name, age, occupation, donation, id):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.donation = donation
        self.id = id

profiles = []


def start():

    print("Welcome to the National Cathederal Donations Platform !")
    print(f"\t1. Create new profile\n\t2. Display Profile Details\n\t3. Edit Existing profile\n\t4. Delete Profile\n\t5. General Information\n\tx. Exit")

    

    while True:
        choice1 = input("* Select an option: ")

        match choice1:
            case '1':
                def add():
                    new_profile = create_profile()
                    profiles.append(new_profile) # Adds profile object to object list

                while True:
                    add()
                    user_choice = input("Do you want to add another profile? (y/n): ").lower() # Always be lowercased
                    match user_choice:
                        case 'y':
                            add()
                            break
                        case 'n':
                            break
                        case _:
                            "Enter either 'y' or 'n'"
                # Printing info for individual profiles after exiting data entry loop
                print("Profiles:")
                for profile in profiles: #For an object in the list
                    print("Name:", profile.name)
                    print("Age:", profile.age)
                    print("Occupation:", profile.occupation)
                    print("Donation: $",profile.donation)
                    print("Your ID is: ", profile.id)
                    print()
                start()
                    
                break   
            case '2':
                profile_details()
                break
            case '3':
                edit_profile()
                break
            case '4':
                delete_profile()
                break
            case '5':
                general_info()
                break
            case 'x':
                print("Exiting the platform...")
                break  
            case _:
                print("Invalid choice. Please enter a number from '1-6' or x ")

        

"""Functions: SET 1"""
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



# Stores return values in their respective variables 
result = calculate_totals(profiles)
total_donations = result[0]
total_num = result[1]







def profile_details():
    #Incomplete
    print(f"\t1. Get profile deatils by ID\n\t2. Get profile details by name\n\t0. Back\n\tX. Exit")

    while True:
        choice1 = input("* Select an option: ")

        match choice1:
            case '1':
                getProfileByID()
                break  
            case '2':
                getProfileByName()
                break
            case '0':
                start()
                break
            case 'x':
                print("Exiting the platform...")
                break  
            case _:
                print("Invalid choice. Please enter a number from '0-2' or x ")



def edit_profile():
    #Incomplete
    print("Incomplete")



def delete_profile():
    #Incomplete
    print("Incomplete")


def general_info():
    print(f"\nTotal Donation: ${total_donations:.2f}")
    print(f"Number of Donations: {total_num}")  




"""Functions: SET 2"""

def getProfileByID():
    #Incomplete
    print("Incomplete")

def getProfileByName():
    #Incomplete
    print("Incomplete")




start()



    


# COMPLETED
"""
- Create new profile for donator (Name, Age, Occupation, Donation, Random ID)
- Save profile with OOP
- Create multiple identifiable profiles (random ID should be for Identification)
- More interactive session (each input leads you to a function)


"""


# Future of this program
"""
- Correct Total Donation amount + Number of Donations
- Get profile by ID (Function)
- Get profile by name (Function)
- Edit Profile Details (Function)

# Function to show profile based on id

"""

