#!/usr/bin/env python3

#
# In order for this to work, you must have the csv setup so that it is ordered: deviceid, serialnumber, ou, assetid
# and preferably named master.csv. if not, make sure to change the name for the master_csv variable
#
#       Exact GAM command to run:  gam print cros deviceid serialnumber ou assetid > master.csv
#
#


import csv, os


#clear screen for mac os / linux device
os.system('clear')

#Prompt user input
csv_name = input('Please enter the name of the csv you need data for: ')
os.system('clear')

#i adjust in my search algorithm for the average user not knowing that computers start with 0. So technically
#the first column is 0, but they'll (hopefully) put 1 etc. 
column_number = input('What column is the serial number in? (#s only): ')
#check valid user input
if int(column_number) not in range(1,100):
    print('Please only enter a number. Try again.')
    exit()
os.system('clear')

print('What type of info do you need?')
data_type = input('1) Device IDs   3) OU   4) Asset IDs (as listed in G Suite) : ')
#Check valid user input
if data_type not in ['1','3','4']:
    print('Please only enter a number to make a selection')
    exit()
os.system('clear')

output_csv = input('Please give the output file a name (including.csv): ')

#Create output csv files
f = open(output_csv, "w")
f.close()

#setup master spreadsheet
master_csv = 'master.csv'

#Open up both .csv and dump into a lists
r1 = csv.reader(open(csv_name)) # Here your csv file
r2 = csv.reader(open(master_csv))
lines_need = list(r1)
lines_all = list(r2)

#Set some counters for positions in the csv files as I'm reading through
row_need = 0
row_all = 0

#tally cells that were fixed
good = 0
fixed = 0

#add new column header
lines_need[0].append(lines_all[0][int(data_type)-1])

#Goes through and checks if current serial number matches the serial number in that row, if it does
#it copies over the corresponding data found, master sheet must be setup as deviceid, serialnumber, ou, assetid to work
#i also subtract 1 off the column number to adjust as stated earlier
for need_line in open(csv_name):
    for all_line in open(master_csv):

        if lines_need[row_need][int(column_number)-1].lower() in all_line.lower():
            lines_need[row_need].append(lines_all[row_all][int(data_type)-1])
            fixed += 1

        row_all += 1

    row_need += 1
    row_all = 0

#write resulting list to csv
with open(output_csv,'w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(lines_need)

print('Done')
print('Added ', fixed,' items to the spreadsheet.')
