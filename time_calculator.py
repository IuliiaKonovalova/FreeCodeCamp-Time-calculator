def add_time(start, duration, day=False):
    new_time = ''
    final_hours = ''
    final_minutes = ''
    final_meridiem = ''
    final_day = ''
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
    initial_hour, initial_minutes = list(map(int, initial_time.split(':')))
    # Getting initial hours and minutes

    duration_hour, duration_minutes = list(map(int, duration.split(':')))
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
        final_hours = final_hours % 24
        
        if final_day == 1:
            day_references = '(next day)'
        else:
            day_references = f'({final_day} days later)'
    
    # Checking AM PM
    if final_hours == 0:
        final_meridiem = 'AM'
        final_hours = 12
    elif final_hours >= 12:
        final_meridiem = 'PM'
        if final_hours > 12:
            final_hours -= 12
    else:
        final_meridiem = 'AM'
    
    # Formating minutes
    final_minutes = str(final_minutes).zfill(2)


    # Check whether day of the week was given and final_day was assigned 
    if day and final_day:
        day = day.lower().capitalize()
        #  Check whether the spelling is correct
        if day in days_of_week:
            # Match the day to the index in the list
            day_index = days_of_week.index(day)
            # Getting the day of the week
            new_day = final_day % 7
            # if day isn't changed
            if new_day == 0:
                if day_references == '':
                    new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day}'
                else:
                    new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day} {day_references}'
            # if day is changed
            else:
                day = days_of_week[(day_index + new_day) % 7]
                if day_references == '':
                    new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day}'
                else:
                    new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day} {day_references}'
    # Check whether only day of the week was given
    elif day:
        day = day.lower().capitalize()
        if day in days_of_week:
            day_index = days_of_week.index(day)
            if day_references == '':
                    new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day}'
            else:
                new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}, {day} {day_references}'
    #  Otherwise just use hours, minutes, AM/PM, +/- day references
    else:
        if day_references == '':
            new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()}'
        else:
            new_time = f'{final_hours}:{final_minutes} {final_meridiem.strip()} {day_references}'

    return new_time