import re

# Available destinations
places = {
    "Karnataka": ["Dakshina Kannada", "Uttara Karnataka", "Silicon City"],
    "Mumbai": ["Historical Places", "Modern Mumbai"],
    "Goa": ["Old Goa", "New Goa"]
}

# Trip batches and their dates
trip_batches = {
    "Batch Arjuna": "12/03/2025",
    "Batch Udaan": "21/03/2025",
    "Batch Safar": "13/04/2025",
}

# Pricing details
price_details = {
    "Karnataka": 5000,
    "Mumbai": 8000,
    "Goa": 7000,
}

print("Welcome to our Tourist Company!")
print("\nAvailable Destinations:")
for place in places:
    print("-", place)

# Getting the destination choice
choose_place = input("\nEnter the destination you want to travel: ").strip().title()

if choose_place in places:
    print("\nHere are some places you can visit in", choose_place + ":", ", ".join(places[choose_place]))
else:
    print("\nInvalid destination. Please restart and enter a valid place.")
    exit()

# Display available batches
print("\nAvailable Batches and Dates:")
for batch, date in trip_batches.items():
    print(f"- {batch}: {date}")

chosen_batch = input("\nEnter your preferred batch name: ").strip().casefold()

# Validate batch name
batch_names = {k.casefold(): k for k in trip_batches}
if chosen_batch not in batch_names:
    print("\nInvalid batch name. Please restart and enter a valid batch.")
    exit()

chosen_batch = batch_names[chosen_batch]  # Get correct case-sensitive batch name

# Get the number of people
try:
    num_people = int(input("\nEnter the number of people traveling: "))
    if num_people <= 0:
        print("\nNumber of travelers must be greater than 0. Please restart.")
        exit()
except ValueError:
    print("\nInvalid input. Please enter a valid number.")
    exit()

# Collect customer contact details
email = input("\nEnter your email address: ").strip()
contact_number = input("Enter your 10-digit contact number: ").strip()

# Email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
if not re.match(email_pattern, email):
    print("\nInvalid email address. Please restart and enter a valid email.")
    exit()

# Contact number validation
if not (contact_number.isdigit() and len(contact_number) == 10):
    print("\nInvalid contact number. Please restart and enter a valid 10-digit number.")
    exit()

# Calculate total price based on age discounts
total_price = 0

for i in range(num_people):
    try:
        age = int(input(f"\nEnter the age of traveler {i+1}: "))
    except ValueError:
        print("\nInvalid input. Please restart and enter a valid number for age.")
        exit()

    if age <= 5:
        print("Traveler is under 5 years old – Free of charge.")
    elif 6 <= age <= 12:
        total_price += price_details[choose_place] * 0.5  # 50% discount
    elif age >= 60:
        total_price += price_details[choose_place] * 0.7  # 30% discount
    else:
        total_price += price_details[choose_place]  # Full price

# Display booking details
print("\n====== Booking Confirmation ======")
print(f"Destination: {choose_place}")
print(f"Batch: {chosen_batch} ({trip_batches[chosen_batch]})")
print(f"Total Travelers: {num_people}")
print(f"Total Price: ₹{total_price}")
print(f"Email: {email}")
print(f"Contact: {contact_number}")
print("Thank you for choosing our service! Have a great trip!")