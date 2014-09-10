def deal_time(file):
    (hour,min) = file.split(':')
    return(hour*60+min)
