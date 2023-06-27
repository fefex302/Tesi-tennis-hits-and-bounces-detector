import csv
import sys
import getopt

#file_name: nome del file csv dal quale leggere i dati
#output: nome del file csv che verrà creato
#window: finestra di frame che andremo a considerare (otterrò 3 * window nuove colonne)
#interval: intervallo con cui salteremo n frame prima di passare alla prossima finestra, esempio:
#   se interval = 5 e window = 15 allora per il primo ciclo considererò i frame dal primo al 15esimo, nel secondo considererò
#   dal frame 6 (1+5) al frame 21 (6+15)
#bounce_start: inizio del punto della finestra da cui voglio iniziare a considerare se c'è stato un salto
#bounce_end: fine del punto della finestra da cui voglio iniziare a considerare se c'è stato un salto
#questi ultimi due parametri si usano in questo modo: consideriamo una finestra di 15 frame, se bounce_start = 5 e bounce_end=9:
#  0 1 2 3 4 [5 6 7 8 9] 10 11 12 13 14   (si noti come il conto del frame parte da 0)

try:
    (opts, args) = getopt.getopt(sys.argv[1:], '', [
        'file_name=',
        'output=',
        'x_res=',
        'y_res=',
        'window=',
        'interval=',
        'bounce_start=',
        'bounce_end='
    ])
    if len(opts) != 8:
        raise ''
except:
    print('er')
    print('usage: python3 newcsvread.py --file_name=<videoPath> --output=<outputPath> --x_res-<xres> --y_res=<yres> --window=<window> --interval=<interval> --bounce_start=<starting_frame> --bounce_end=<ending_frame>')
    exit(1)

for(opt,arg) in opts:
    if opt == '--file_name':
        filename = arg
    elif opt == '--x_res':
        xres = arg
    elif opt == '--y_res':
        yres = arg
    elif opt == '--window':
        window = int(arg)
    elif opt == '--interval':
        interval = int(arg)
    elif opt == '--output':
        output = arg
    elif opt == '--bounce_start':
        bounce_start = int(arg)
    elif opt == '--bounce_end':
        bounce_end = int(arg)
    else:
        print('usage: python3 newcsvread.py --file_name=<videoPath> --output=<outputPath> --x_res-<xres> --y_res=<yres> --window=<window> --interval=<interval> --bounce_start=<starting_frame> --bounce_end=<ending_frame>')
        exit(1)

if bounce_start >= window:
    print('bad input')
    exit(1)
if bounce_end >= window or bounce_end <=bounce_start:
    print('bad input')
    exit(1)

field = []
for i in range(0,window):
    field.append('Vis' + str(i))
    field.append('X' + str(i))
    field.append('Y' + str(i))
field.append('Bounce')
print(field)

tmp = []
iter = 0

with open(filename,'r') as csvinput:
    with open(output, 'w+') as csvoutput:
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
                for i in range(0,window):
                    row = next(reader)
                    tmp.append(row[1])
                    x = round((int(row[2])/int(xres))*100,3)
                    tmp.append(str(x))
                    y = round((int(row[3])/int(yres))*100,3)
                    tmp.append(str(y))

                    #se ho un miss nella finestra etichetto sempre come misstrack
                    if int(row[5])== 3:
                        bounce = '3'
                        miss = True

                    if miss == False and bounce_start <= i <= bounce_end:
                        if int(row[5]) == 1:
                            bounce = '1'
                        elif int(row[5]) == 2:
                            bounce = '2'

                tmp.append(bounce)
                writer.writerow(tmp)
                tmp = []
                iter = iter + 1
                csvinput.seek(0)
            except Exception as e:
                print(e)
                break




