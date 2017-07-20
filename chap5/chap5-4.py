def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)

    return(mins + '.' + secs)

    
with open ('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')
with open("julie.txt") as juf:
    data = juf.readline()
julie = data.strip().split(',')
with open ("mikey.txt") as mif:
    data = mif.readline()
mikey = data.strip().split(',')
with open("sarah.txt") as saf:
    data = saf.readline()
sarah = data.strip().split(',')



james = sorted(set([sanitize(each_c) for each_c in james]))
julie = sorted(set([sanitize(each_c) for each_c in julie]))
mikey = sorted(set([sanitize(each_c) for each_c in mikey]))
sarah = sorted(set([sanitize(each_c) for each_c in sarah]))


"""use set to unique the data"""
        

print(james[0:3])
print(julie[0:3])
print(mikey[0:3])
print(sarah[0:3])

