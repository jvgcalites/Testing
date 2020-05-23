import matplotlib.pyplot as plt
from _csv import reader


# Load a CSV file
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset


f1, f2, f3, f4, f5, gx, gy, gz, ax, ay, az = ([] for i in range(11))
# Make a prediction with KNN on Iris Dataset
filename = 'data.txt'
dataset = load_csv(filename)
for i in dataset:
    print(i)
    # parse the data
    # values = i.split(",")
    # contents of values array are string
    # convert them to double/decimal and append to the list
    f1.append(float(i[0]))
    f2.append(float(i[1]))
    f3.append(float(i[2]))
    f4.append(float(i[3]))
    f5.append(float(i[4]))
    gx.append(float(i[5]))
    gy.append(float(i[6]))
    gz.append(float(i[7]))
    ax.append(float(i[8]))
    ay.append(float(i[9]))
    az.append(float(i[10]))

sampleData = len(dataset)  # 30 samples per label
print(sampleData)
dataPoint = list(range(1, sampleData + 1, 1))
# plot the data
# plt.figure()
# flex sensors
#plt.subplot(221)
plt.plot(dataPoint, f1, 'c', # pinky
         dataPoint, f2, 'm', # ring
         dataPoint, f3, 'y', # middle
         dataPoint, f4, 'k', # pointy
         dataPoint, f5, 'g') # thumb
plt.xlabel("Data Points")
plt.ylabel("Flex Sensor Values")
plt.title("Flex Sensors")
plt.grid(True)
plt.show()

# gyroscope
#plt.subplot(222)
plt.plot(dataPoint, gx, 'c',
         dataPoint, gy, 'm',
         dataPoint, gz, 'y', )
plt.xlabel("Data Points")
plt.ylabel("Gyroscope Values")
plt.title("Gyroscope")
plt.grid(True)
plt.show()

# accelerometer
#plt.subplot(223)
plt.plot(dataPoint, ax, 'c',
         dataPoint, ay, 'm',
         dataPoint, az, 'y', )
plt.xlabel("Data Points")
plt.ylabel("Accelerometer Values")
plt.title("Accelerometer")
plt.grid(True)
plt.show()
