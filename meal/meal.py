def main():
    str = input("What time is it? ")
    time_in_hours = convert(str)
    if 7<= time_in_hours <=8: print("breakfast time")
    elif 12<= time_in_hours <=13: print("lunch time")
    elif 18<= time_in_hours <=19: print("dinner time")
    else: print("")

def convert(time):
    hours = 0.0
    minutes = 0.0
    midday = ""
    if time.find(":") != -1:
        if "a.m." in time or "p.m." in time:
            hours, minutes = time.split(":")
            minutes, midday = minutes.split(" ")

            hours = float(hours)
            minutes = float(minutes)

            if midday == "p.m." and hours != 12.00:
                hours += 12
            elif midday == "a.m." and hours == 12:
                hours = 0
        else:
            hours, minutes = time.split(":")

    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()
