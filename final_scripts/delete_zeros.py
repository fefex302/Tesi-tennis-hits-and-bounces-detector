import csv

#script che elimina la riga prima e quella dopo un colpo o un rimbalzo

def delete_rows(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        all = []
        found = False
        delete_last = True
        i = 0
        for row in reader:
            #print(found)

            if(i == 0 or i == 1):
                all.append(row)
            else:
                if(row[-1] == '1' or row[-1] == '2'):
                    if(found):
                        all.append(row)
                        delete_last = False
                    else:
                        found = True
                        if(delete_last):
                        #print(all[-1])
                            all.pop()
                        #print(all[-1])
                        all.append(row)
                        delete_last = False
                elif(found):
                    found = False
                    continue
                else:
                    all.append(row)
                    delete_last = True
            i += 1
        writer.writerows(all)

# Example usage
delete_rows('./finale/finale_tennis_8_9_hit_miss.csv', './finale/finale_tennis_8_9_hit_miss_skip.csv')
