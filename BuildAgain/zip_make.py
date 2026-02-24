import pathlib
import zipfile

def ZipCreate(filePaths,location):
    try:
        dest = pathlib.Path(location,"compress.zip")

        with zipfile.ZipFile(dest,'w') as archive:
            for file_path in filePaths:
                file_path = pathlib.Path(file_path)
                archive.write(file_path,arcname=file_path.name)
    except Exception as e:
        print("Error",e)