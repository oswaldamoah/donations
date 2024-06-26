import random

class Profile: # Constructor
    def __init__(self, name, age, occupation, donation, id):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.donation = donation
        self.id = id

profiles = [] # List of profile objects


def start():

    print("CleanEarth™ Ghana | Donations Platform") # Header
    print(f"\t1. Create new profile\n\t2. Display Profile Details\n\t3. Edit Existing profile\n\t4. Delete Profile\n\t5. General Information\n\tx. Exit")
    # Multiple choice prompt

    while True:
        choice1 = input("* Select an option: ")
        print("")


        match choice1:
            case '1':
                def add():
                    new_profile = create_profile()
                    profiles.append(new_profile) # Adds profile object to object list
                add()
                while True:
                    print("")
                    user_choice = input("Do you want to add another profile? (y/n): ").lower() # Always be lowercased
                    print("")
                    if user_choice == 'y':
                        add()
                    elif user_choice == 'n':
                        break
                    else:
                        print("Enter either 'y' or 'n'")

                # Printing info for individual profiles after exiting data entry loop
                print("Profiles:")
                for profile in profiles: #For an object in the list
                    print("Name:", profile.name)
                    print("Age:", profile.age)
                    print("Occupation:", profile.occupation)
                    print("Donation: $",profile.donation)
                    print("Your ID is: ", profile.id)
                    print("")

                goHome() # Allows to easily go home or exit after each fxn
                break
            case '2':
                profile_details()
                goHome()
                break
            case '3':
                id = input("Enter ID of profile you want to edit: ")
                edit_profile(id)
                goHome()
                break
            case '4':
                id = input("Enter ID of profile you want to delete: ")
                delete_profile(id)
                goHome()
                break
            case '5':
                general_info()
                goHome()
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
            donation = float(input("Enter donation amount: $"))
            break  # Exit loop on successful conversion to float
       except ValueError:
            print("Invalid donation amount. Please enter a number.")

    id = f"DON-{random.randint(24001, 24100)}"  # Unique ID for donation

    
    return Profile(name, age, occupation, donation, id)






def profile_details():
    #Incomplete
    print(f"\t1. Get profile deatils by ID\n\t2. Get profile details by name\n\t0. Back\n\tX. Exit")

    while True:
        choice2 = input("* Select an option: ")
#
        match choice2:
            case '1':
                id = input("Enter your ID: ")
                getProfileByID(id)
                break  
            case '2':
                name = input("Enter your name: ")
                getProfileByName(name)
                break
            case '0':
                start()
                break
            case 'x':
                print("Exiting the platform...")
                break  
            case _:
                print("Invalid choice. Please enter a number from '0-2' or x ")
                



def edit_profile(id):
    found_profile = None
    for profile in profiles:
        if profile.id.lower() == id.lower():
            found_profile = profile
            break  # Exit the loop after finding a match
    if found_profile:
        print(f"Edit: \n\t1. Name\n\t2. Age\n\t3. Occupation\n\t4. Donation\n\t0. Back\n\tX. Exit")
    
    # Fxns that edit naem, age, etc.
    # They are in the edit profile fxn so that they can access 'found_profile' 
    def edit_name(e_name):
        found_profile.name = e_name

    def edit_age(e_age):
        found_profile.age = e_age

    def edit_occupation(e_occupation):
        found_profile.occupation = e_occupation

    def edit_donation(e_donation):
        found_profile.donation = e_donation


    while True:
        choice1 = input("* Select an option: ") # For earlier Multiple Choice prompt
        print("")
        
#
        match choice1:
            case '1':
                # Edit name
                print(f"Current name: {found_profile.name} for ID({found_profile.id})")
                e_name = input("Enter new name: ")
                edit_name(e_name) # changes value of name
                print(f"Name for ID({found_profile.id}) has been changed to {found_profile.name}")
                break  
            case '2':
                # Edit age
                print(f"Current age: {found_profile.age} years for ID({found_profile.id})")
                e_age = input("Enter new age: ")
                edit_age(e_age) # changes value of age
                print(f"Age value for ID({found_profile.id}) has been changed to {found_profile.age} years")
                break
            case '3':
                # Edit occupation
                print(f"Current occupation: {found_profile.occupation} for ID({found_profile.id})")
                e_occupation = input("Enter your occupation: ")
                edit_occupation(e_occupation) # changes value of occupation
                print(f"Occupation for ID({found_profile.id}) has been changed to {found_profile.occupation}")
                break  
            case '4':
                # Edit donation
                print(f"Current donation: ${found_profile.donation} for ID({found_profile.id})")
                try:
                    e_donation = float(input("Enter your donation value: $")) # changes value of donation when input is a float/number
                except ValueError:
                    print("Invalid donation amount. Please enter a number.")
                edit_donation(e_donation)
                print(f"Donation value for ID({found_profile.id}) has been changed to ${found_profile.donation}")
                break
            case '0':
                start()
                break
            case 'x':
                print("Exiting the platform...")
                break  
            case _:
                print("Invalid choice. Please enter a number from '0-4' or x ")






def delete_profile(id):

    found_profile = None
    for profile in profiles:
        if profile.id.lower() == id.lower():
            found_profile = profile
            break  # Exit the loop after finding a match

    if found_profile:
        profiles.remove(found_profile)
        print(f"{found_profile.name}'s profile has been deleted")
    else:
        print(f"No profile with id {id} was found")


def general_info():
    total_donation = 0
    num_donors = 0
    for profile in profiles:
        total_donation += profile.donation
        if profile.donation > 0:  # Check if donation is greater than 0 (they donated)
            num_donors += 1

    print("General Donation Information:")
    print(f"Total amount of Donations: ${total_donation:.2f}")  # Format to 2 decimal places
    print(f"Total no. of donors: {num_donors}")





"""Functions: SET 2"""

def getProfileByID(id):
    # each object has a unique ID, so when ID is inputted, the program searches for just one object
    found_profile = None
    for profile in profiles:
        if profile.id.lower() == id.lower():
            found_profile = profile
            break  # Exit the loop after finding a match

    if found_profile:
        print("")
        print("Name:", found_profile.name)
        print("Age:", found_profile.age)
        print("Occupation:", found_profile.occupation)
        print("Donation: ", found_profile.donation,"USD")
        print("")
    else:
        print("Profile Not Found")



def getProfileByName(name):
    # searches for all strings matching the input, puts their corresponding objects in a list and prints their properties 
    found_profiles = [] 
    for profile in profiles: 
        if name.lower() in profile.name.lower():  # Search for substring (case-insensitive)
         found_profiles.append(profile) # adds to 

    if found_profiles:
        print("Profiles matching the search:")
        for profile in found_profiles:
            print("")
            print("Name:", profile.name)
            print("Age:", profile.age)
            print("Occupation:", profile.occupation)
            print("Donation:", profile.donation, "USD")
            print("")
    else:
        print("No profiles found matching the search")

def goHome():
    print("")
    
    while True:
        decision = input("Homepage-'0' | Exit-'x' : ")
        print("")

        match decision:
            case '0':
                start()
                break
            case 'x':
                break
            case _:
                print("Enter either '0 - Home' or 'x - Exit'")
            


start()



    


# COMPLETED
"""
- Create new profile for donator (Name, Age, Occupation, Donation, Random ID)
- Save profile with OOP
- Create multiple identifiable profiles (random ID should be for Identification)
- More interactive session (each input leads you to a function)
- Get profile by ID (Function)
- Get profile by name (Function)
- Edit Profile Details (Function)
- Correct Total Donation amount + Number of Donations


- ReadMe file
"""

