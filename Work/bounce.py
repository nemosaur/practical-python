# bounce.py
#
# Exercise 1.5
height = 100
bounce_count=0

while bounce_count<10:
    height=height*3/5
    bounce_count+=1
    print(round(bounce_count,4),round(height,4))
    