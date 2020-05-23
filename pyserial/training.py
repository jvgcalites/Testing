import serial
import matplotlib.pyplot as plt
import numpy as np

ser = serial.Serial('COM5', baudrate=9600, timeout=1)
sampleData = 45  # 30 samples per label
dataPoint = list(range(1, sampleData + 1, 1))
print(dataPoint)

label = input('Enter the label: ')
while label != "exit":
    f1, f2, f3, f4, f5, gx, gy, gz, ax, ay, az = ([] for i in range(11))
    dataList = []
    i = 0
    while i < sampleData:
        rawData = ser.readline().decode('ascii')
        if rawData != "":
            i += 1
            # remove "#" and "~" and "/n"
            data = ""
            data = rawData[1:len(data) - 3]
            # store all data for saving later
            dataList.append(data)
            # parse the data
            values = data.split(",")
            # contents of values array are string
            # convert them to double/decimal and append to the list
            f1.append(float(values[0]))
            f2.append(float(values[1]))
            f3.append(float(values[2]))
            f4.append(float(values[3]))
            f5.append(float(values[4]))
            gx.append(float(values[5]))
            gy.append(float(values[6]))
            gz.append(float(values[7]))
            ax.append(float(values[8]))
            ay.append(float(values[9]))
            az.append(float(values[10]))
            print("%s. %s" % (i, data))
    # plot the data
    plt.figure()
    # flex sensors
    plt.subplot(221)
    plt.plot(dataPoint, f1, 'c',
             dataPoint, f2, 'm',
             dataPoint, f3, 'y',
             dataPoint, f4, 'k',
             dataPoint, f5, 'g')
    plt.xlabel("Data Points")
    plt.ylabel("Flex Sensor Values")
    plt.title("Flex Sensors")
    plt.grid(True)

    # gyroscope
    plt.subplot(222)
    plt.plot(dataPoint, gx, 'c',
             dataPoint, gy, 'm',
             dataPoint, gz, 'y',)
    plt.xlabel("Data Points")
    plt.ylabel("Gyroscope Values")
    plt.title("Gyroscope")
    plt.grid(True)

    # accelerometer
    plt.subplot(223)
    plt.plot(dataPoint, ax, 'c',
             dataPoint, ay, 'm',
             dataPoint, az, 'y', )
    plt.xlabel("Data Points")
    plt.ylabel("Accelerometer Values")
    plt.title("Accelerometer")
    plt.grid(True)
    plt.show()

    # save or not save?
    saveData = input("Do you wish to save the data? (y/n) : ")
    if saveData == 'y':
        f = open("data.txt", "a+")
        for data in dataList:
            f.write("%s,%s\n" % (data, label))
        f.close()
    label = input('Enter the label: ')
