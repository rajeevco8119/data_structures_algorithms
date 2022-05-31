# Time conversion 12 hour format to 24 hour format
def timeConversion(s):
    time = s[:-2]
    if s[8] == 'A':
        if s[0] == '1' and s[1] == '2':
            return '00'+time[2:]
        return time
    elif s[8] == 'P':
        if s[0] == '1' and s[1] == '2':
            return time
        hour = int(time[0]+time[1])
        hour += 12
        new_time = str(hour)+time[2:]
        return new_time
