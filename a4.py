weather=(0,0,0,1,1,0,1)
s=0   #sunnyweather
r=0   #rainyweather
for day in range(0,7):
    if(weather[day]==0):
        r=r+1
    else:
        s=s+1

if(s > r):
    print("Great weather in the city for a week")
else:
    print("Poor weather in the city for a week")