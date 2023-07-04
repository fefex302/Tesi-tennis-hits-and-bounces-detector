#script per generare il dataset con la media delle finestre

import csv
import sys


if(len(sys.argv) != 6):
    print('run as: "python3 sumxy.py <input.csv> <output.csv> <window> <bounce_start> <bounce_end>"')
    exit(1)

input = sys.argv[1]
output = sys.argv[2]
window = int(sys.argv[3])
bounce_start = int(sys.argv[4])
bounce_end = int(sys.argv[5])

new = []

with open(input,'r') as csvinput:
    with open(output, 'w+') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput,lineterminator='\n')
        writer.writerow(['X1','Y1','X2','Y2','X3','Y3','Bounce'])
        row = next(reader)

        try:
            while(True):
                x1,x2,x3 = [0,0,0]
                timesx1,timesx2,timesx3= [0,0,0]
                y1,y2,y3 = [0,0,0]
                timesy1,timesy2,timesy3 = [0,0,0]
                ctrl = 0
                row = next(reader)
                for k in range(0,window*3):
                    if(k<=bounce_start*3):
                        if(ctrl == 1):
                            if(float(row[k]) != 0):
                                x1 = x1 + float(row[k])
                                timesx1 = timesx1 +1
                            ctrl = 2 
                        elif(ctrl == 2):
                            if(float(row[k]) != 0):
                                y1 = y1 + float(row[k])
                                timesy1 = timesy1 +1
                            ctrl = 0
                        else:
                            ctrl = 1
                    elif(bounce_start*3<k<(bounce_end*3)+3):
                        if(ctrl == 1):
                            if(float(row[k]) != 0):
                                x2 = x2 + float(row[k])
                                timesx2 = timesx2 +1
                            ctrl = 2 
                        elif(ctrl == 2):
                            if(float(row[k]) != 0):
                                y2 = y2 + float(row[k])
                                timesy2 = timesy2 +1
                            ctrl = 0
                        else:
                            ctrl = 1
                    else:
                        if(ctrl == 1):
                            if(float(row[k]) != 0):
                                x3 = x3 + float(row[k])
                                timesx3 = timesx3 +1
                            ctrl = 2 
                        elif(ctrl == 2):
                            if(float(row[k]) != 0):
                                y3 = y3 + float(row[k])
                                timesy3 = timesy3 +1
                            ctrl = 0
                        else:
                            ctrl = 1
                new.append(round((x1/timesx1),3))
                new.append(round((y1/timesy1),3))
                new.append(round((x2/timesx2),3))
                new.append(round((y2/timesy2),3))
                new.append(round((x3/timesx3),3))
                new.append(round((y3/timesy3),3))
                new.append(row[window*3])
                writer.writerow(new)
                new = []
                                                  
                          
        except Exception as e:
                print(e)
                
