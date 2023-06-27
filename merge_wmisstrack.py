import csv

#script per fare il merge delle annotazioni di colpi e rimbalzi con quelle dei misstrack

def merge_miss(input_miss, input_hit, output_file):
    with open(input_miss, 'r') as missfile, open(input_hit) as hitfile, open(output_file, 'w', newline='') as outfile:
        
        missfl = csv.reader(missfile)
        hitfl = csv.reader(hitfile)
        writer = csv.writer(outfile)

        tmp_miss = next(missfl)
        tmp_hit = next(hitfl)
        writer.writerow(tmp_miss)

        try:
            while(True):
                tmp_miss = next(missfl)
                tmp_hit = next(hitfl)
                if tmp_miss[-1] == '3':
                    tmp_hit[-1] = '3'
                    print(tmp_hit)
                    writer.writerow(tmp_hit)
                else:
                    writer.writerow(tmp_hit)
        except:
            print('finished')
            
# Example usage
merge_miss('./finale/tennis_9_miss.csv', './new_dataset/tennis_9_final.csv','./finale/tennis_9_hit_miss.csv')