"""首先打开一个文件，在人名和话语之间加上一个said：
其次解决语句中多个：的情况，给split加上参数1，只分2次
然后的问题是有pause，没有：，需要判断下语句中是否有："""

try:
    data = open('C:/Users/lenovo/pystudy/chap3/sketch.txt')

    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print (' said: ', end='')
            print (line_spoken,end='')
        except:
            pass

    data.close()

"""使用异常处理来解决"""

except:
    print('The data file is missing!')
