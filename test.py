import re
f=open('hebing - short - 99out - short.csv','r')

fo=open('hebing - short - 99out - short_out.csv','w')

lines=f.readlines()
fo.write(lines[0])
for line in lines[1:]:
    infos=line.split(',')
    tot=0
    try:
        for i in range(8,57+8):
            tot+=float(infos[i])
        fo.write(line.strip()+','+str(tot)+'\n')

    except:
        fo.write(line)
        pass

f.close()
#fo.close()
