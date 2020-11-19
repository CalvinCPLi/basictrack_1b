#2.8
time_now = int(input("What time is it now? (In 24 hour format)"))
timer_duration = int(input("How long do you want a timer for?"))
time_end = ((timer_duration + time_now) % 24)
print("It will be", time_end, "O' Clock")