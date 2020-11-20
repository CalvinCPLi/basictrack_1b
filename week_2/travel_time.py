distance = float(input("What is the distance to your destination?"))
option = input("What is your preferred method of travel? Walking, Biking or Driving?")
if option == "Walking":
    speed_walking = float(input("What is your speed while walking? (in km/h)"))
    travel_time_walking = distance / speed_walking
    print(travel_time_walking, "minute(s)")
elif option == "Biking":
    speed_biking = float(input("What is your average speed while biking? (in km/h)"))
    travel_time_biking = distance / speed_biking
    print(travel_time_biking, "minute(s)")
elif option == "Driving":
    speed_driving = float(input("What is your average speed while driving?"))
    travel_time_driving = distance / speed_driving
    print(travel_time_driving, "minute(s)")






