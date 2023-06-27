import csv
import sys
import json
#script che prende come input file json e file csv di tracknet e crea un nuovo csv con le annotazioni unite al csv di tracknet 
#0 niente
#1 rimbalzo
#2 colpo
#3 misstrack

if(len(sys.argv) != 4):
    print('run as: "python3 csvread.py <file.json> <input.csv> <output.csv> "')
    exit(1)

jsonfile = sys.argv[1]
input = sys.argv[2]
output = sys.argv[3]

#apro il json e mi salvo i frame in un array
f = open(jsonfile)
data = json.load(f)
num_videos = len(data)
#print(num_videos)

bounces = []
hit = []
miss = []
for i in range(0,num_videos):
    num_frames = len(data[i]['box'])
    for k in range(0,num_frames):
        if(len(data[i]['box'][k]['sequence'])!=0):
            if(data[i]['box'][k]['labels'][0] == 'Bounce'):
                bounces.append(data[i]['box'][k]['sequence'][0]['frame'])
            elif(data[i]['box'][k]['labels'][0] == 'Miss'):
                miss.append(data[i]['box'][k]['sequence'][0]['frame'])
            else:
                hit.append(data[i]['box'][k]['sequence'][0]['frame'])

            

#creo il nuovo csv con i frame del rimbalzo
with open(input,'r') as csvinput:
    with open(output, 'w+') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        all = []
        row = next(reader)
        row.append('Bounce')
        all.append(row)

        for row in reader:
            if(int(row[0]) in bounces):
                row.append('1')
                print(row)
            elif(int(row[0]) in hit):
                row.append('2')
                print(row)
            elif(int(row[0]) in miss):
                row.append('3')
                print(row)
            else:
                row.append('0')
                print(row)
            all.append(row)

        writer.writerows(all)

f.close
csvinput.close
csvoutput.close
print(bounces)
print(hit)
print(miss)