def add_time(start, duration, *day):
    new_time = ''
    new_hour = ''
    new_minute = ''
    new_meridiem = ''
    new_day = ''
    day_of_week = ''
    day_statement = ''
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Getting initial hours and minutes
    initial_time, meridiem = start.split()
    meridiem.upper()
    initial_time.split(':')
    initial_hour = int(initial_time[0])
    initial_minutes = int(initial_time[1])
    
    # Getting initial hours and minutes
    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_minutes = int(duration_time[1])







    return new_time