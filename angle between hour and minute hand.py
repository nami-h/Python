def angle(h, m):
    if (h<0 or m<0 or h>12 or m>59):
        exit("Wrong input")
        
    if(h==12):
        h=0
    if(m==60):
        m=0
    hour_angle=0.5*(h*60+m)
    minute_angle=6*m
    
    angle=abs(hour_angle-minute_angle)
    angle=min(360-angle, angle)

    return angle

print(angle(12, 30))
