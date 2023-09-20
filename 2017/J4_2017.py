times = [34, 71, 83, 95, 107, 119, 130, 142, 154, 166, 178, 201, 213, 225, 237, 260, 272, 284, 296, 331, 341, 355, 402, 390, 414, 461, 473, 520, 532, 591, 671]
minutes=int(input(""))
counter=0
if minutes>671:
    loop=minutes//720
    minutes-=loop*720
    counter+=len(times)*loop

closest=int(min(times,key=lambda x:abs(x-minutes)))
if minutes>closest or minutes==closest:
    counter+=times.index(closest)+1
elif minutes<closest:   
    counter+=times.index(closest)
print(counter)