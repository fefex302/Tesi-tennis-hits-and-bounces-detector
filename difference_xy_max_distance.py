import csv
import sys
import math

#crea il dataset con la differenza fra il primo e ultimo frame delle finestre, in più calcola la media della finestra centrale e la massima distanza percorsa

def first_last(ctrl,row,k,firstlast,avg=None):
    if(ctrl == 0):
        return 
    elif(ctrl == 1):
        if(float(row[k])!= 0):
            if(firstlast[0] == 0):
                firstlast[0] = float(row[k])
            else:
                firstlast[1] = float(row[k])
            if(avg!=None):
                avg[0] += float(row[k])
                avg[1] += 1
        return
    else:
        if(float(row[k])!= 0):
            if(firstlast[2] == 0):
                firstlast[2] = float(row[k])
            else:
                firstlast[3] = float(row[k])
            if(avg!=None):
                avg[2] += float(row[k])
                avg[3] += 1
        return

def distanza_euclidea(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    if(len(sys.argv) != 6):
        print('run as: "python3 sumxy.py <input.csv> <output.csv> <window> <bounce_start> <bounce_end>"')
        exit(1)

    input = sys.argv[1]
    output = sys.argv[2]
    window = int(sys.argv[3])
    bounce_start = int(sys.argv[4])
    bounce_end = int(sys.argv[5])
    with open(input,'r') as csvinput:
        with open(output, 'w+') as csvoutput:
            reader = csv.reader(csvinput)
            writer = csv.writer(csvoutput,lineterminator='\n')
            writer.writerow(['X1','Y1','X2','Y2','X3','Y3','AvgX','AvgY','MaxDistance','Bounce'])
            row = next(reader)
            try:
                while(True):
                    new = []
                    maxdistance = 0
                    prec =[0,0]
                    firstlast = [0,0,0,0]
                    it = 0
                    x = 0

                    for tmp in row:
                        if it == 0:
                            if tmp == '0':
                                prec = [0,0]
                                it = -2
                            else:
                                it +=1

                        elif it == 1:
                            if prec[0] == 0:
                                prec[0] = float(tmp)
                            else:
                                x = float(tmp)
                            #    difference = abs(prec[0] - float(tmp))
                            #    if difference > maxdistance[0]:
                            #        maxdistance[0] = difference
                            #    prec[0] = float(tmp)
                            it +=1

                        elif it == 2:
                            it = 0
                            if prec[1] == 0:
                                prec[1] = float(tmp)
                            else:
                                y = float(tmp)
                                difference = distanza_euclidea(x,y,prec[0],prec[1])
                                if difference > maxdistance:
                                    maxdistance = difference
                                prec[1] = float(tmp)

                        else:
                            it +=1
                    row = next(reader)
                    ctrl = 0
                    for k in range(0,bounce_start*3):
                        first_last(ctrl,row,k,firstlast)
                        ctrl = (ctrl + 1)%3
                    new.append(round(firstlast[0]-firstlast[1],3))
                    new.append(round(firstlast[2]-firstlast[3],3))
                    
                    #media x e y finestre centrali [sumx,timesx,sumy,timesy]
                    avg = [0,0,0,0]

                    firstlast = [0,0,0,0]
                    for k in range(bounce_start*3,(bounce_end*3)+3):
                        first_last(ctrl,row,k,firstlast,avg)
                        ctrl = (ctrl + 1)%3
                    new.append(round(firstlast[0]-firstlast[1],3))
                    new.append(round(firstlast[2]-firstlast[3],3))                   
                    firstlast = [0,0,0,0]

                    for k in range((bounce_end*3)+3,window*3):
                        first_last(ctrl,row,k,firstlast)
                        ctrl = (ctrl + 1)%3
                    new.append(round(firstlast[0]-firstlast[1],3))
                    new.append(round(firstlast[2]-firstlast[3],3))
                    new.append(round(avg[0]/avg[1],3))
                    new.append(round(avg[2]/avg[3],3))
                    new.append(round(maxdistance,3))
                    new.append(row[window*3])
                    writer.writerow(new)

            except Exception as e:
                print(e)




if __name__ == '__main__':
    main()
