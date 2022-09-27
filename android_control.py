from ppadb.client import Client as AdbClient
from androidAutomate import Device
import io
client = AdbClient(host='127.0.0.1', port=5037)
devices = client.devices()
device = devices[0]

#TODO automate this step



myDevice = Device("192.168.10.140:40345")
screenWidth=myDevice.screenWidth
screenHeight=myDevice.screenHeight
screen_real_measurements = [6.7,13.5]
testx = [0.9,2.5,4.2,5.8]
#testy = [3.8,4.9,6,7.2]
testy = [7.2,6,4.9,3.8]
array_of_letters = "stnčmtarčnvsnnnz"
coord = []
matrix_of_letters = [array_of_letters[0:4],array_of_letters[4:8],array_of_letters[8:12],array_of_letters[12:16]]
for index,line in enumerate(matrix_of_letters):
     for indey,letter in enumerate(line):
         coord.append([testx[index],testy[indey]])


f = io.open("words.txt", mode="r", encoding="utf-8")
words = f.read()
words = words.split(" ")
for word in words:
    for letter in word:
        position = array_of_letters.find(letter)
        #print(coord[position][0]*screen_real_measurements[0],coord[position][1]*screen_real_measurements[1])
        myDevice.inputTap(coord[position][0]*screen_real_measurements[0],coord[position][1]*screen_real_measurements[1],percent=True)


