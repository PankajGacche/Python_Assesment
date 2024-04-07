# importing the modules
import os
import shutil
import time;
import datetime
import operator

def copy_src_to_dest(Source,Destination):
    try:
        source_files = os.listdir(Source) #Fetching the list of all the files from Source to copy and paste to destination.
    except:
        print("Source folder not found.") 
    try:
        dest_files = os.listdir(Destination) #Fetching the list of all the files from Destination to check files are already present.
    except:
        print("Destination folder not found.")  

    current_timestamp = time.time() #Get current timestamp to attach filename to achive uniquness if file already present.
    timestamp = datetime.datetime.fromtimestamp(current_timestamp).strftime("%H%M%S") #Formatting timstamp value.
    
    empty_set = set() #Declaring empty set to store the list of all the files from Destination.
    
    for file_name in dest_files:
        empty_set.add(file_name) # adding all destination files to set.

    for file_name in source_files: #Iterating all files from Source to paste Destination.
        count = operator.countOf(empty_set, file_name)
        if(count==1): #Checking file is already present at Destination.
            shutil.copy(Source+file_name, Destination+timestamp+"_"+file_name) #Adding timestamp to already preset files to achieve uniquness.
        else:
            shutil.copy(Source+file_name, Destination+file_name) #Copy file from Source to Destination.
    
    if(len(source_files)>0):
        print("Files are copied successfully from source to destination.")
    else:
        print("Files are not found at Source.")
      
Source = 'D:\\Pankaj\\Study\\Source\\'
Destination = 'D:\\Pankaj\\Study\\Destination\\'

copy_src_to_dest(Source,Destination)


    
 

   

