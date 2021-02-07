import sys
f=open('airlines.csv','r')
f.readline()
d = {}
code,name,year,stats='','',0,0
for line in f.readlines():
    l = line.split(',')
    code,name,year,stats = l[0],','.join(l[1:-2]),l[-2],l[-1]
    if code in d:
        d[code][-1]+=1
    else:
        d[code] = [name,year,stats,0]
f.close()
mincode=[name,d[code][-1]]
maxcode=[name,d[code][-1]]
#json='{\n'+',\n'.join([d[key][0]+": "+str(d[key][-1]) for key in d])+'\n}'
json='{\n'
for key in d:
    if(d[key][-1]<mincode[-1]):
        mincode[0]=d[key][0]
        mincode[1]=d[key][-1]
    if(d[key][-1]>maxcode[-1]):
        maxcode[0]=d[key][0]
        maxcode[1]=d[key][-1]
    json+=d[key][0]+": "+str(d[key][-1])+',\n'
json=json[:-2]+'\n}'
print(json)
print(maxcode[0],maxcode[1])
print(mincode[0],mincode[1])
    

