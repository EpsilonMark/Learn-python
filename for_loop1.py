 #forloop

def loop1():
    for i in range(0,11,1) :
        print(i)

def loop2():
    for i in range(1,11,1) :
        print(i)

def loop3():
    for i in range(1,11,2) :
        print(i)
        print('------------')


def loop_string():
    s = 'over the rainbow'
    for c in s :
        print(c.upper())

def loop_tuple():
    flower = 'lily','jasmine','rose','ivy'
    for f in flower :
        print(f.capitalize())

def loop_tuple2():
    flower = 'lily','jasmine','rose','ivy'
    for i in range(len(flower)) :
        print(i+1,flower[i].capitalize())


loop_tuple2()

# loop_string()

