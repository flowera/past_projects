# -*- coding: utf-8 -*-
"""
Remove Leading and Trailing Spaces of CSV files in particular folders.
Created on Wed Jul 19 15:25:26 2017
@author: GuoRubing
"""

import inspect, os, glob 
import csv

# Change this line to whatever folder you want to revise 
folder_name = "201706 Implants\\"
# Implant data backup folder
implant_dir = "\\\\hosp1serv1\\SS_OPERSCH\\Databases\\Epic_Implants_Database\\Epic_Downloads\\Implants\\"
directory = os.path.join(implant_dir, folder_name)

#rm all the files having their file name containing fixed.
filenames = glob.glob(directory + "*fixed*.csv")
for filename in filenames: 
	os.remove(filename)
filenames = glob.glob(directory + "*.xlsx")
for filename in filenames: 
	os.remove(filename)
	
#Rewrite .cvs files to remove leading and trailing spaces in cells of the corresponding .csv files.


for root,dirs,files in os.walk(directory):
	for file in files:
	    if file.endswith(".csv"):
			name = file.split('.')
			new_name = name[0]+'_fixed.csv'
			in_file = directory + file
			out_file = directory + new_name
			f1 = open(in_file, "rb")
			f2 = open(out_file, "wb")
			row_reader = csv.reader(f1)
			row_writer = csv.writer(f2)
			
			#https://stackoverflow.com/questions/8746908/why-does-csv-file-contain-a-blank-line-in-between-each-data-line-when-outputting
			#row_writer = csv.DictWriter(f2, delimiter=',', lineterminator='\n', fieldnames=headers)
			for row in row_reader:
				new_row = [col.strip() for col in row]
				row_writer.writerow(new_row)
			f1.close()
			f2.close()	
print("Task finished!")		
"""
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]    
	
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:         
                r.append(subdir + "\\" + file)                                                                         
    return r  
"""

""" 
#https://geonet.esri.com/thread/18501
import csv
#directory = os.path.join("C:\\Users\\GuoRubing\\Documents\\Python\\", "python_scripts\\")
#print(os.path.basename(directory)) # python_scripts <- whatever is left at the end of the string, stripped by \.
#print(os.path.dirname(directory)) # C:\\Users\\GuoRubing\\Documents\\Python
#print(directory) # C:\\Users\\GuoRubing\\Documents\\Python\\python_scripts

in_file = "\\\\hosp1serv1\\SS_OPERSCH\\Databases\\Epic_Implants_Database\\Epic_Downloads\\Implants\\201601_Implants\\cap_info.csv"
out_file = "\\\\hosp1serv1\\SS_OPERSCH\\Databases\\Epic_Implants_Database\\Epic_Downloads\\Implants\\201601_Implants\\cap_info_fixed.csv"

f1 = open(in_file, "rb")
f2 = open(out_file, "wb")

row_reader = csv.reader(f1)
row_writer = csv.writer(f2)

for row in row_reader:
	new_row = [col.strip() for col in row]
	#print row, "->", new_row
	#print(', '.join(new_row))
	row_writer.writerow(new_row)
f1.close()
f2.close()	
"""
	
"""
import csv
with open('C:\\Users\\GuoRubing\\Documents\\Python\\python_scripts\\test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print('|'.join(row))
"""
