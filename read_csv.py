import csv
import numpy as np
f=open('train_xy.csv','r')
reader=csv.reader(f)
data=[]
for item in reader:
    data.append(item)

data.pop(0)

datax=[]
for cust in data:
    datax.append(cust[3:])
datax=np.array(datax)

datay=[]
for cust in  data:
    datay.append([cust[2]])
datay = np.array(datay)

f2=open('test_all.csv','r')
reader2=csv.reader(f2)
data2=[]
for item in reader2:
    data2.append(item)

data2.pop(0)

data_test=[]
for cust in data:
    data_test.append(cust[2:])
data_test=np.array(data_test)

data_cust=[]
for cust in  data:
    data_cust.append([cust[0]])
data_cust = np.array(data_cust)

# f=open('out.csv','w')
# headers=['cust','y']
# writer=csv.DictWriter(f,headers)
# writer.writerrows(zip(data_cust,datay[:10000]))

out_cust_no=[]
for data in data_cust:
    out_cust_no.append(data.tolist()[0])

print(out_cust_no)

out_test_ans=[]
for data in datay:
    out_test_ans.append(data[0])


headers = ['label', 'youtube_id']
with open('out.csv', 'w') as f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(out_cust_no)
    f_csv.writerows(out_test_ans)
