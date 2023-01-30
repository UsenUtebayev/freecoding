import time
x = [(h, m, s) for h in range(24) for m in range(60) for s in range(60)]
for d in x:
    time.sleep(1)
    print(f"{d[0]}:{d[1]}:{d[2]}")
