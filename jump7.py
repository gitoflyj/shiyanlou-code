i = 1
while i <= 100:
    if i % 7 == 0 or i % 10 == 7:
        i=i+1
    elif i // 10 ==7:
        i=i+1
    else:
        print(i)
        i=i+1
