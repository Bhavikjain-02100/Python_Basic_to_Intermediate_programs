def can_ride(height, adult_present):
    if height >= 48:
        return True
    elif 42 <= height < 48:
        return adult_present
    else:
        return False
height = int(input("Enter the height in inches: "))
adult_present = input("Is an adult present (yes/no): ").strip().lower() == 'yes'
print(can_ride(height, adult_present))
