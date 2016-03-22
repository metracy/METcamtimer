import sys
import os
import csv
import subprocess as sp
import datetime
import time

#fmpeg -f video4linux2 -i /dev/video11 -vframes 1 test.jpeg

subj = sys.argv[1]#raw_input('Subject#--> ')
cnum = sys.argv[2]#raw_input('Camera#--> ')
sleep = [0,34,26,47,83,147,263,467,830,1477,2626]
tindex = ['0000','0034','0060','0107','0190','0337','0600','1067','1897','3374','6000']

def main():
    i=0
    t=0
    print('Started at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while i <= (len(sleep)-1):
        print(t,"Seconds Elapsed, Sleeping for ", sleep[i], "seconds")
        time.sleep(sleep[i])
        t += sleep[i]
        try:
            filename = "Subject" + str(subj) + "_" + datetime.datetime.now().strftime("%Y-%m-%d") + "_" + tindex[i] + "Sec_" + ".jpeg"
            sp.check_output(['ffmpeg', '-f', 'video4linux2','-video_size','320x240', '-i', '/dev/video' + str(cnum), '-vframes', '1', '/home/inhalant/Desktop/Dropbox/CameraSetup/images/' + str(filename), '-y'])
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        except:
            time.sleep(5)
            filename = "Subject" + str(subj) + "_" + datetime.datetime.now().strftime("%Y-%m-%d") + "_" + tindex[i] + "Sec_" + ".jpeg"
            sp.check_output(['ffmpeg', '-f', 'video4linux2','-video_size','320x240', '-i', '/dev/video' + str(cnum), '-vframes', '1', '/home/inhalant/Desktop/Dropbox/CameraSetup/images/' + str(filename), '-y'])
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        i += 1
    print('Finished at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
main()
