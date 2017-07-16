"""这是“nester.py”模块，提供了一个名为print_lol()的函数，
这个函数的作用是打印列表，其中可能包含（也可能不包含）嵌套列表"""
def print_lol(the_list,indent= False,level= 0):
    """这个函数取一个位置参数，名为"the_list",这可以是python列表。所指定的
列表上的每个数据输出到屏幕上，各个数据占一行。
第二个参数用来打印制表符，带默认为0.
新增参数用于判断是否需要缩进。"""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='')
            print(each_item)

