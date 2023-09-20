speed_limit=int(input("Enter the speed limit: "))
car_speed=int(input("Enter the recorded speed of the car: "))
if speed_limit>=car_speed:
    print("Congratulations, you are within the speed limit!")
else:
    difference=car_speed-speed_limit
    if difference<=20:
        print("You are speeding and your fine is $100.")
    elif difference>=21 and difference<=30:
        print("You are speeding and your fine is $270.")
    elif difference>=31:
        print("You are speeding and your fine is $500.")