def circle_area(x):
    area = x**2*3.14
    return area
  
def circle_circum(y):
    circum = y*2*3.14
    return circum

ans=int(input("請輸入半徑?"))
circlearea=circle_area(ans)
circlecircum=circle_circum(ans)
print("圓面積:"+str(circlearea))
print("圓周長:"+str(circlecircum))