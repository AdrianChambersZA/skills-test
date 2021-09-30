def number_to_hours_and_minutes(number):
    if number < 60:
        hours = 0
        minutes = number
    else:
        hours = number // 60
        minutes = number % 60
    if hours == 1:
        hour_text = " hour, "
    else:
        hour_text = " hours, "
    if minutes == 1:
        minute_text = " minute"
    else:
        minute_text = " minutes"
    return str(hours) + hour_text + str(minutes) + minute_text

number_to_hours_and_minutes(133)