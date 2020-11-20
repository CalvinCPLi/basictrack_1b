# get distance to destination
distance = float(input("What is the distance to your destination?"))
# ask what method of transport the user will take
option = input("What is your preferred method of travel? Walking, Biking or Driving?")
if option == "Walking":
    speed_walking = float(input("What is your speed while walking? (in km/h)"))
    travel_time_walking = distance / speed_walking
    travel_time_walking_minutes = travel_time_walking * 60
    print(travel_time_walking, "hours or", travel_time_walking_minutes, "minute(s)")
elif option == "Biking":
    speed_biking = float(input("What is your average speed while biking? (in km/h)"))
    travel_time_biking = distance / speed_biking
    travel_time_biking_minutes = travel_time_biking * 60
    print(travel_time_biking, "minute(s)")
elif option == "Driving":
    speed_driving = float(input("What is your average speed while driving?"))
    travel_time_driving = distance / speed_driving
    travel_time_driving_minutes = travel_time_driving * 60
    parking_spot_distance = float(input("What is the distance from the parking lot to the destination? in m"))
    speed_walking = float(input("What is your speed while walking? (in km/h)"))
    speed_walking_ms = speed_walking / 3.6
    travel_time_parking = (parking_spot_distance / speed_walking_ms) / 60
    travel_time_parking_seconds = travel_time_driving * 60
    print(travel_time_driving, "hours or", travel_time_driving_minutes, "minute(s) to your destination and",
          travel_time_parking, "minute(s) or", travel_time_parking_seconds, "second(s) to the door!")
