import re
hand=open('data_file.txt')
sum=0
for line in hand:
    line=line.rstrip()
    digi=re.findall('[0-9]+',line)
    li=digi
    if(len(li)>=1):
        for i in li:
             sum=sum+int(i)

       

print(sum)

	    	



	    





