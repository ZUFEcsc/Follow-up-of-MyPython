paper_width = 0.00008
mountain_width = 8848.13
cnt = 0
while True:
    paper_width *= 2
    cnt += 1
    if paper_width >= mountain_width:
        break

print("需要对折"+str(cnt)+"次才可以")