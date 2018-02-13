"""
Name: Spend Report
Author: GuoRubing
Date: Oct. 12, 2017
"""
import os,csv
import pandas as pd
import numpy as np
#import openpyxl as xl
#from shutil import copyfile
in_file = 'C:\\Users\\GuoRubing\\Google Drive\\Python\\uams_reports_test\\test.csv'
out_file = 'C:\\Users\\GuoRubing\\Google Drive\\Python\\uams_reports_test\\test_cp.csv'
#path3 = 'C:\\Users\\GuoRubing\\Google Drive\\Python\\uams_reports_test\\'

#df = pd.read_csv("C:/Users/GuoRubing/Google Drive/Python/uams_reports_test/test.csv")
df = pd.read_csv("C:\\Users\\GuoRubing\\Google Drive\\Python\\uams_reports_test\\test.csv")
print (len(df.index))
df.tail(1)
"""
1. rm zero qty rows
"""
df_sap = df[df['Qty Paid'] != 0]

"""
2. Add MPN-UOM
"""
s1 = df_sap['MatGrp']
s2 = df_sap['U O M']
df_sap['MPN-UOM'] = s1.str.cat(s2, sep = '-')

# Last Tab
s1 = df_sap['Manufacturer Part No']
s2 = df_sap['U O M']
s3 = df_sap['MPN-UOM']
s4 = df_sap['Date PO Created']
s5 = df_sap['Description']
s6 = df_sap['Unit Price less Dist Fee']
df_last = pd.concat([s3, s4, s5, s6], axis=1)
df_last = df_last.sort_values(['Date PO Created', 'MPN-UOM'],ascending = [0,1])
df_last.drop_duplicates(subset = ['MPN-UOM'], keep = 'first')
pd.merge(df_SAP, df_last, left_on = 'MPN-UOM', right_on = 'MPN-UOM', how='left')


"""
f_in = open(in_file, "r")
f_out = open(out_file, "w", newline = '')
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
row_reader = csv.reader(f_in)
row_writer = csv.writer(f_out)
for row in row_reader:
	new_row = [col.strip() for col in row]
	#print (row, "->", new_row)
	print(', '.join(new_row))
	row_writer.writerow(new_row)
f_in.close()
f_out.close()
#  copy a File: https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python?noredirect=1&lq=1
#  copyfile(path1, path2)

"""
