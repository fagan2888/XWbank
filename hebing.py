from keras.models import Sequential
from keras.layers import Dense, Activation
import time
import csv
import numpy as np
f = open('super_short.csv', 'r')
reader = csv.reader(f)
data = []
for item in reader:
    data.append(item)
data.pop(0)


def getdata(data, xy, iftest=0):
    datax = []
    if iftest == 0:
        x = 0
        e = 15000
        y_pos=2
    else:
        x = 15001
        e = 25001
        y_pos=0
    for cust in data[x:e]:
        if xy == 'x':
            datax.append(cust[3:])
        if xy == 'y':
            datax.append([cust[y_pos]])
    datax = np.array(datax)
    return datax


datax = getdata(data, 'x')
datay = getdata(data, 'y')
data_test = getdata(data, 'x', 1)
data_cust = getdata(data, 'y', 1)

# f2=open('test_all.csv','r')
# reader2=csv.reader(f2)
# data2=[]
# for item in reader2:
#     data2.append(item)
#
# data2.pop(0)
#
# data_test=[]
# for cust in data2:
#     data_test.append(cust[2:])
# data_test=np.array(data_test)
#
# data_cust=[]
# for cust in  data2:
#     data_cust.append([cust[0]])

t0 = time.time()
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Activation('relu'))
# For a single-input model with 2 classes (binary classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=16))  # 38 ,157//112
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])


# Train the model, iterating on the data in batches of 32 samples

print(datax)
print(datay)
model.fit(datax, datay, epochs=30, batch_size=15000)
result = model.predict(data_test, batch_size=15000)
print(result)
result_list = result.tolist()

with open('out_hebing.csv', 'w') as f:
    f.write('cust_id,pred_prob\n')
    for i in range(10000):
        outstring = str(data_cust[i][0]) + ',' + str(round(float(result_list[i][0]), 8)) + '\n'
        f.write(outstring)

print('time=', time.time() - t0)
