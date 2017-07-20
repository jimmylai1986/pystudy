def sanitize(time_string):
    """用.替换时间当中的- ："""
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)

"""定义函数读取数据"""

def get_coach_data(file_name):
    try:
        with open (file_name) as f:
            data= f.readline()
        return (data.strip().split(','))
    except IOError as ioerr:
        print("File error:" + str(ioerr))
        return(None)
    



james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')


"""use set to unique the data"""
        

print(sorted(set([sanitize(each_c) for each_c in james]))[0:3])
print(sorted(set([sanitize(each_c) for each_c in julie]))[0:3])
print(sorted(set([sanitize(each_c) for each_c in mikey]))[0:3])
print(sorted(set([sanitize(each_c) for each_c in sarah]))[0:3])

