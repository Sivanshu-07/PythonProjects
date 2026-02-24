<<<<<<< HEAD
import pathlib
import zipfile

#filePaths : files that needs to be compressed
#destDir : Location where the compressed file will save
def zipCreate(filePaths, destDir): 
    try:
        dest = pathlib.Path(destDir, 'compressed.zip') # this means in location destDir, the compressed file will be saved as compressed.zip
        #dest has only address not zip file, till now zip file is not created

        with zipfile.ZipFile(dest, 'w') as archive:
            for file_path in filePaths:
                file_path = pathlib.Path(file_path) # this line will convert the filepath(that was initially in string) to proper path
                archive.write(file_path, arcname=file_path.name) # this line means put the files to archive 
                # imagine archive as a box in which we will put the compressed files into
                # arcname means what will be the name of the compressed file in that archive folder
                # arcname is basically used to give the name to compressed file in that folder

    except Exception as e:
=======
import pathlib
import zipfile

#filePaths : files that needs to be compressed
#destDir : Location where the compressed file will save
def zipCreate(filePaths, destDir): # initially destDir is n string format
    try:
        dest = pathlib.Path(destDir, 'compressed.zip') # this means in location destDir, the compressed file will be saved as compressed.zip
        #dest has only address not zip file, till now zip file is not created
        # destDir is now converted to proper path and its address is stored in dest

        #dest is the address so we need to open it to store the compressed file
        with zipfile.ZipFile(dest, 'w') as archive:
            for file_path in filePaths:
                file_path = pathlib.Path(file_path) # this line will convert the filepath(that was initially in string) to proper path
                archive.write(file_path, arcname=file_path.name) # this line means put the files to archive 
                # imagine archive as a box in which we will put the compressed files into
                # arcname means what will be the name of the compressed file in that archive folder
                # arcname is basically used to give the name to compressed file in that folder

    except Exception as e:
>>>>>>> e0d4995 (Added Personal Expense Tracker Project)
        print("Error:", e)