#print('hello world')
#print('tea')
#print('Mark')

#point = 1,7
#print(point[0])
#print(point[1])

#th = 'ThaiLand',5 ,10, 12
#print(th[1]+th[2]+th[3])

def distance(pointA , pointB):
    return ((pointA[0]- pointB[0])**2 +(pointA[1]-pointB[1])**2 ) **.5

pointA = 1,7
pointB = 1,10
d = distance(pointA,pointB)

print(d)