# #greeting.py

# import time
# hour= float(input("ENter the time in 24 hour format: "))
# if hour >=5 and hour<=11.59:
#     print("Good Morning")
# elif hour >=12 and hour<=15.59:
#     print("Good Afternoon")
# elif hour >=16 and hour<=20.59:
#     print("Good Evening")
# elif hour >=21 or hour <=4.59:
#     print("Good Night")
# else:
#     print("Invalid time entered")

import time

hour = int(time.strftime("%I"))
am_pm = time.strftime("%p")

print(f"Current time: {hour} {am_pm}")

if am_pm == "AM" and 5 <= hour < 12:
    print("Good Morning")
elif am_pm == "PM" and 12 <= hour < 4:
    print("Good Afternoon")
elif am_pm == "PM" and 4 <= hour < 9:
    print("Good Evening")
else:
    print("Good Night")
