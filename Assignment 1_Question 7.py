# Time Conversion Function
def seconds_to_time(seconds):
    if seconds < 0 or seconds == 24 * 60 * 60: # a day (24 hours) is equal to 24*60*60 seconds
        return "Invalid number of seconds. Please try again."
        # according to the question, the highest value is in hours
        # therefore if it's over 24 hours then it's invalid

    # convert seconds to different categories
    hours = seconds // 3600
    remaining_seconds = seconds % 3600 # after they're converted into hours, the rest will be used for minutes
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60 # after minutes are converted, the rest which can't converted into a whole number will be seconds

    # determine if the period is AM or PM
    if hours < 12:
        period = "AM" # from 0 to 11 -> AM
    else:
        period = "PM" # from 12 to 24 -> PM (according to a 24-hour time)

    # convert 24-hour to 12-hour clock
    if hours == 0:
        hours = 12
    elif hours > 12: # afternoon time
        hours = hours - 12
        # if its 13 in the afternoon for the 24-hour time, but it's 1PM in 12-hour clock

    return f"{hours} {minutes} {seconds} {period}"

print(seconds_to_time(19067)) # expected output 5 17 47 AM




