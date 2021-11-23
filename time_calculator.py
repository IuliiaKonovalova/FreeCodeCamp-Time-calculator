def add_time(start, duration, *day):
    new_time = ''
    final_hours = ''
    final_minutes = ''
    final_meridiem = ''
    final_day = ''
    day_of_week = ''
    day_references = ''
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

    # Change to military time
    if meridiem == 'PM':
        initial_hour += 12

    # Adding duration to initial time
    final_hours = initial_hour + duration_hour
    final_minutes = initial_minutes + duration_minutes

    # Checking minutes
    if final_minutes >= 60:
        final_hours += 1
        final_minutes -= 60

    # Checking hours
    if final_hours > 24:
        final_day = final_hours // 24
        final_meridiem = 'AM'
        if final_day == 1:
            day_references = '(next day)'
        day_references = f'({final_day} days later)'







    return new_time