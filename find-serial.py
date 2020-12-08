#!/usr/bin/env python3

#
#
#
# csv file must be nammed asset-tiger.csv
#
#
#

import csv

print('Hello')
csv_name = input('Please enter the name of the csv you would like to compare: ')
output_csv = input('Please give the output file a name (including.csv): ')

f = open(output_csv, "w")
f.close()

#set variable for master spreadsheet
master_csv = 'asset-tiger.csv'

#Open up both .csv and dump into a lists
r1 = csv.reader(open(csv_name)) # Here your csv file
r2 = csv.reader(open(master_csv))
lines_check = list(r1)
lines_all = list(r2)

#Set some coutners for positions in the csv files as I'm reading through
row_check = 0
row_all = 0

#tally cells that were fixed
not_found = 0
found = 0


#goes through inventory csv and looks to see if serial number from that csv (in column 5) is located at in current master row
#if not, nothing gets appended and the loop carries on
for check_line in open(csv_name):
    for all_line in open(master_csv):
        if lines_check[row_check][1].lower() in all_line.lower():
            lines_check[row_check].append(lines_all[row_all][5])
            found += 1
            break
        row_all += 1
    row_check += 1
    row_all = 0

with open(output_csv,'w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(lines_check)


print('Done')
print('Found: ', found)
