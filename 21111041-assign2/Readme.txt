Plugins-
Environments: python 3.7.0


Dependencies-
Python Libraries: pandas 1.0.3, numpy 1.18.1, openpyxl, scipy


Programs-

.sh files:

assign2.sh 
top level script that runs the entire assignment

percent-india.sh
runs percent-india.py
Input: DDW-C18-0000.xlsx ,DDW_PCA0000_2011_Indiastatedist.xlsx
Output:  percent-india.csv

gender-india.sh
runs gender-india.py
Input: DDW-C18-0000.xlsx ,DDW_PCA0000_2011_Indiastatedist.xlsx
Output: gender-india-a.csv ,gender-india-b.csv ,gender-india-c.csv

geography-india.sh
runs geography-india.py
Input: DDW-C18-0000.xlsx ,DDW_PCA0000_2011_Indiastatedist.xlsx
Output: geography-india-a.csv, geography-india-b.csv, geography-india-c.csv

3-to-2-ratio.sh
runs 3-to-2-ratio.py
Input: DDW-C18-0000.xlsx
Output: 3-to-2-ratio.csv

2-to-1-ratio.sh
runs 2-to-1-ratio.py
Input: DDW-C18-0000.xlsx
Output: 2-to-1-ratio.csv

age-india.sh
runs age-india.py
Input: DDW-C18-0000.xlsx ,DDW-0000C-14.xls
Output: age-india.csv

literacy-india.sh
runs literacy-india.py
Input: DDW-C19-0000.xlsx ,DDW-0000C-08.xlsx
Output: literacy-india.csv

region-india.sh
runs region-india.py
Input: DDW-C17-2300.xlsx ,DDW-C17-0900.xlsx ,DDW-C17-2200.xlsx ,DDW-C17-1000.xlsx ,DDW-C17-1900.xlsx ,DDW-C17-2100.xlsx ,DDW-C17-2000.xlsx ,DDW-C17-0100.xlsx ,DDW-C17-0300.xlsx ,
       DDW-C17-0200.xlsx ,DDW-C17-0600.xlsx ,DDW-C17-0500.xlsx ,DDW-C17-0700.xlsx ,DDW-C17-0400.xlsx ,DDW-C17-3500.xlsx ,DDW-C17-1800.xlsx ,DDW-C17-1100.xlsx ,DDW-C17-1700.xlsx ,
       DDW-C17-1600.xlsx ,DDW-C17-1200.xlsx ,DDW-C17-1400.xlsx ,DDW-C17-1300.xlsx ,DDW-C17-1500.xlsx ,DDW-C17-2900.xlsx ,DDW-C17-2800.xlsx ,DDW-C17-3300.xlsx ,DDW-C17-3200.xlsx ,
       DDW-C17-3100.xlsx ,DDW-C17-3400.xlsx
Output: region-india-a.csv ,region-india-b.csv 

age-gender.sh
runs age-gender.py
Input: DDW-C18-0000.xlsx ,DDW-0000C-14.xls
Output: age-gender-a.csv ,age-gender-b.csv ,age-gender-c.csv 

literacy-gender.sh
runs literacy-gender.py
Input: DDW-C19-0000.xlsx ,DDW-0000C-08.xlsx
Output: literacy-gender-a.csv ,literacy-gender-b.csv ,literacy-gender-c.csv


How to use:
In order to run all programs sequentially, run the following command from the terminal-
bash assign2.sh 

NOTE: 
1) The programs will run sequentially in the extact order of the .sh file mentioned above. 
