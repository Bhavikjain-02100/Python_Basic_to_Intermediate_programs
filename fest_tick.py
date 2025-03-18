def festival_ticket_price(age, time):
    if age <= 18:
        price = 10
    elif 19 <= age <= 59:
        price = 20
    else:
        price = 15
    if time >= 20:
        price *= 0.5
    return price

age = int(input("Enter age: "))
time = int(input("Enter time in 24-hour format: "))
ticket_price = festival_ticket_price(age, time)
print(f"The ticket price is: ${ticket_price}")
