#This is version one of an automated script to edit all .txt files in a folder
#Then output a folder with files that have commas after each column (No heading on the first three columns)
#Last Edit By Grant Copple, June 2nd 2020

import glob
import os
import sys
import shutil
# Create directory aka an output folder
dirName = 'Fixed'

try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
except FileExistsError:
    #check to see if the directory already exisits
    print("Directory " , dirName ,  " already exists")

# Get the path of our new folder
path = os.path.join(os.getcwd(),dirName)
# Get the files in our current folder
files = glob.glob(os.path.join(os.getcwd(), "*.txt"))

# Open and get information from all files
for File_Name in files:
    with open(File_Name, 'r') as f:
        lines = f.readlines()[23:]

    # Check for errors at the end of the files and delete them
    check = 'Errors/warnings:' in lines[-3]
    if  check:
        del lines[-4:-1]

    # Now we need to add commas in all the right postions
    new_lines = [len(lines)-1]
    for x in range(len(lines)-1):
        new_line = lines[x]
        new_line = new_line[:16] + ',' + new_line[16:33] + ',' + new_line[33:46] + ',' + new_line[46:63] + ',' + new_line[63:80] + ',' + new_line[80:93] + ',' + new_line[93:107] + ',' + new_line[107:122] + ',' + new_line[122:137] + ',' + new_line[137:152] + ',' + new_line[152:162] + ',' + new_line[162:172] + ',' + new_line[172:182]
        new_lines.insert(x,new_line)
    #Now will will create our heading line
    Heading  = "        Latitude,        Longitude,        H-Ell,      CorrTime,        Heading,          Pitch,           Roll,     VEast,    VNorth,       VUp"
    COrd = new_lines[0]
    COrd = COrd[0:50]
    FL = COrd + Heading
    new_lines.insert(0, FL)
    del FL
    
    #Okay now we will write to a new file
    n = len(File_Name) - 4
    New_File_Name = File_Name[:n] + "_CSV.txt"
    with open(New_File_Name,"w") as f:
        for x in range(len(new_lines)-1):
            f.write(new_lines[x]+ '\n')

    #Move files to the right spot
    shutil.move(New_File_Name, path)
del files
del lines
print("All files have been converted. Proceeding to create text files.")

os.startfile("Text_to_Shape_NAD83_2011.gms")
