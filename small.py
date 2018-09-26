# use the conda environmnet
# python 3.6
# tensorflow
from keras.models import Sequential
from keras.layers import Dense, Activation
import time
import csv
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

f=open('train_xy_2.csv','r')
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

f2=open('test_all2.csv','r')
reader2=csv.reader(f2)
data2=[]
for item in reader2:
    data2.append(item)

data2.pop(0)

data_test=[]
for cust in data2:
    data_test.append(cust[2:])
data_test=np.array(data_test)

data_cust=[]
for cust in  data2:
    data_cust.append([cust[0]])



t0=time.time()
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Activation('relu'))
# For a single-input model with 2 classes (binary classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=38))#  38 ,157
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
#data = np.random.random((1000, 100))
#labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples

print(datax)
print(datay)
model.fit(datax, datay, epochs=10, batch_size=256)
result=model.predict(data_test,batch_size=256)
print(result)
result_list=result.tolist()


with open('out01.csv', 'w') as f:
    f.write('cust_id,pred_prob\n')
    for i in range(10000):
        outstring=str(data_cust[i][0])+','+str(round(float(result_list[i][0]),8))+'\n'
        f.write(outstring)

print('time=',time.time()-t0)