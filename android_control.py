from ppadb.client import Client as AdbClient
from androidAutomate import Device
import io
import time

"""
Script for inputting words into android SPAR application
To be clear this script is really poorly writen
"""
client = AdbClient(host='127.0.0.1', port=5037)
devices = client.devices()
device = devices[0]


def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


myDevice = Device("192.168.10.140:38821")
screenWidth=myDevice.screenWidth
screenHeight=myDevice.screenHeight
screen_real_measurements = [6.7,14]
testx = [1.7,2.8,3.9,5]
testy = [6.8,7.7,8.5,9.2]
array_of_letters = "stnčmtarčnvsnnnz"
coord = []
matrix_of_letters = [array_of_letters[0:4],array_of_letters[4:8],array_of_letters[8:12],array_of_letters[12:16]]
for indey,line in enumerate(matrix_of_letters):
    for index,letter in enumerate(line):
         coord.append([testx[index],testy[indey]])

f = io.open("words.txt", mode="r", encoding="utf-8")
words = f.read()
words = words.split(" ")
duplicated_words = []
for word in words:
    #Skip words with duplicated letters, can't be bothered
    if set(i for i in word if word.count(i)>1):
        duplicated_words.append(word)
        print('Add this words manually',duplicated_words)
        next
    else:
        for letter in word:
            position = array_of_letters.find(letter)
            x = coord[position][0] / screen_real_measurements[0] * screenWidth
            y = coord[position][1] / screen_real_measurements[1] * screenHeight
            myDevice.inputTap(x, y)
    input_word_x = 4.6/screen_real_measurements[0]*screenWidth
    input_word_y = 10.4/screen_real_measurements[1]*screenHeight
    myDevice.inputTap(input_word_x,input_word_y)
    time.sleep(0.5)


