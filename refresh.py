import os,time,random 

while True:
    os.system("am start -n com.walid.far/.MainActivity")
    time.sleep(random.randint(5,10))
    os.system("am start -n com.walid.back/.MainActivity")
    time.sleep(random.rantint(10,50))


