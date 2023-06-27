#con questo script è possibile analizzare nuovi video mai visti dai modelli

import joblib
import sys
import csv
import subprocess
import pandas as pd
import difference_xy
from sklearn.ensemble import RandomForestClassifier

if(len(sys.argv) < 3):
    print('run as: "python3 RF.py <tracknet_dataset.csv> <video> <x_res> <y_res>"')
    exit(1)

tracknetcsv = sys.argv[1]
video = sys.argv[2]
window = 15
interval = 5
xres = int(sys.argv[3])
yres = int(sys.argv[4])

#carico il modello allenato su altri video
RF = joblib.load('./final_scripts/RF.joblib')

field = []
field.append('Row')
for i in range(0,window):
    field.append('Vis' + str(i))
    field.append('X' + str(i))
    field.append('Y' + str(i))
field.append('Bounce')
print(field)

tmp = []
iter = 0
riga = 1

#qua creo il primo dataset, quello con 15*3 colonne + 1 che sarebbe il numero della riga
with open(tracknetcsv,'r') as csvinput:
    with open("./final_scripts/video_dataset.csv", 'w+') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput,lineterminator='\n')
        writer.writerow(field)
        row = next(reader)
        print(row)
        while(True):
            try:
                for k in range(0,iter*interval + 2):
                    row = next(reader)
                bounce = '0'
                
                miss = False
                tmp.append(riga)
                for i in range(0,window):
                    row = next(reader)
                    tmp.append(row[1])
                    x = round((int(row[2])/xres)*100,3)
                    tmp.append(str(x))
                    y = round((int(row[3])/yres)*100,3)
                    tmp.append(str(y))

                riga += 1
                tmp.append(bounce)
                writer.writerow(tmp)
                tmp = []
                iter = iter + 1
                csvinput.seek(0)
            except Exception as e:
                print(e)
                break

#filtraggio
arguments = ['./final_scripts/video_dataset.csv', './final_scripts/video_dataset_filter.csv', '15']
subprocess.call(['python','./final_scripts/filter_csv.py'] + arguments)

#creazione dataset con differenze
arguments = ['./final_scripts/video_dataset_filter.csv', './final_scripts/video_dataset_difference.csv', '15', '5','9']
subprocess.call(['python','./final_scripts/difference_xy_predict.py'] + arguments)


ball = pd.read_csv('./final_scripts/video_dataset_difference.csv', sep=',', header=0)
columns = len(ball.columns) - 1
ball.head()
X = ball.iloc[:,1:columns]
print(X)
prediction = RF.predict(X)
column_array = ball.iloc[:, 0]


rows = column_array.values


iter = 0
for tmp in prediction:
    if(tmp == 1 or tmp == 2):
        prediction[iter-1] = 0
    iter +=1
print(prediction)

with open('./final_scripts/video_dataset.csv', 'r') as csvinput:
    with open('./final_scripts/video_dataset_final.csv','w+') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput,lineterminator='\n')
        row = next(reader)
        writer.writerow(row)
        
        number = 0
        while(True):
            try:
                row = next(reader)
                if int(row[0]) == rows[number]:
                    row[-1] = prediction[number]
                    number +=1
                writer.writerow(row)
            except Exception as e:
                print(e)
                break

#ricreo il formato del dataset di tracknet con le predizioni del modello
with open('./final_scripts/video_dataset_final.csv', 'r') as csvinput:
    with open('./final_scripts/video_dataset2.csv','w+') as csvoutput:
        reader = csv.reader(csvinput)
        writer = csv.writer(csvoutput,lineterminator='\n')
        row = next(reader)
        print(row)
        labels = ['Vis','X','Y','Bounce']
        writer.writerow(labels)
        iteration = 0
        all = []
        quad = []
        while(True):
            try:
                iteration += 1
                all = []
                quad = []
                row = next(reader)
                if iteration == 1:
                    for i in range(1,31):
                        if 1 <= i <= 15:
                            if(i%3 == 0):
                                quad.append(row[i])
                                quad.append('0')
                                all.append(quad)
                                quad = []
                            else:
                                quad.append(row[i])

                        elif 15 < i :
                                if(i%3 == 0):
                                    quad.append(row[i])
                                    quad.append(row[-1])
                                    all.append(quad)
                                    quad = []
                                else:
                                    quad.append(row[i])
                    writer.writerows(all)
                else:
                    for i in range(16,31):
                        if(i%3 == 0):
                            quad.append(row[i])
                            quad.append(row[-1])
                            all.append(quad)
                            quad = []
                        else:
                            quad.append(row[i])
                    writer.writerows(all)
            except Exception as e:
                print(e)
                break

#creazione del nuovo video
arguments = [video, './final_scripts/video_dataset2.csv', './final_scripts/output.mp4']
subprocess.call(['python','./final_scripts/RFvideo_generator.py'] + arguments)