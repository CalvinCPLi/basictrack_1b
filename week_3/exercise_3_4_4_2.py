week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_today = int(input("What day is it today? (0-6)"))
days_staying = int(input("How many days are you staying?"))
days = days_staying % 6
print("It will be a", week_days[days + day_today])