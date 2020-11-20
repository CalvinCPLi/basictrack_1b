#2.8
time_now = float(input("What time is it now? (In 24 hour format)"))
timer_duration = float(input("How long do you want a timer for?"))
time_end = ((timer_duration + time_now) % 24.00)
print("It will be", time_end, "O' Clock")