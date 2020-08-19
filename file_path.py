import os.path
if os.path.isfile("abs.txt"):
    print("存在")
    file=open("abs.txt","a")
    file.write("檔案94存在")
else:
    print("不存在")
    file=open("abs.txt","w")
    file.write("這是新的檔案")
file.close()
