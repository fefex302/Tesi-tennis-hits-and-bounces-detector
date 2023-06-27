import csv
import sys

#prende il csv e lo filtra, bisogna passare la lunghezza della sequenza (15 frame nel nostro caso) e di quanto vogliamo filtrare ogni finestra (es 2 elimina ogni
# riga che non ha almeno 2 frame prima 2 dentro e 2 dopo quella centrale)

if(len(sys.argv) != 4):
    print('run as: "python3 filter_csv.py <file.csv> <output.csv> <window> <filter>"')
    exit(1)

input = sys.argv[1]
output = sys.argv[2]
window = int(sys.argv[3])
filter = int(sys.argv[4])
all = []

with open(input,'r') as inp, open(output,'w+') as out:
    writer = csv.writer(out,lineterminator='\n')
    reader = csv.reader(inp)
    for row in reader:
        pre = 0
        inside = 0
        after = 0
        for tmp in row[:window]:
            if(tmp=='1'):
                pre = pre + 1
        for tmp in row[window:window*2]:
            if(tmp=='1'):
                inside = inside + 1
        for tmp in row[window*2:window*3]:
            if(tmp=='1'):
                after= after + 1
        if(pre>1 and inside>1 and after>1):
            all.append(row)
            print(row)
        
    writer.writerows(all)