score = []
name = []
maxscore = 0
minscore = 100
maxname=""
minname=""
totle = 0
time=int(input("人數?"))
times = 0
for i in range(time):
    times=times+1
    now = int(input("分數"+str(times)+"?"))
    nowname = input("名稱"+str(times)+"?")
    name.append(nowname)
    score.append(int(now))
    if now > maxscore:
        maxscore=now
        maxname=nowname
    if now < minscore:
        minscore=now
        minname=nowname
    totle=totle+now
pin=totle/len(score)
print("總分"+str(totle))
print("平均"+str(pin))
print("最高分"+str(maxscore)+maxname)
print("最低分"+str(minscore)+minname)