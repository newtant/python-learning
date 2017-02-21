import os

mainPath = os.getcwd()
folders = []

def warn():
    print("---")
    print(" -> WARNING:")
    print("---")
    print("This will move every single file from all sub-directories into the current folder.")
    print("After that it will delete every single sub-directory.")
    print("Are you sure you want to do that?.")
    print("---")
    if input("[Y/n] >> ") == "Y":
        return 0
    else:
        return 1

def move_from_subdirs():
    for folder, subdirs, fileList in os.walk(mainPath):
        if folder != mainPath:
            folders.append(folder)
        for fileName in fileList:
            os.rename(os.path.join(folder, fileName), os.path.join(mainPath, fileName))

def delete_subdirs():
    for folder in sorted(folders, reverse=True):
        os.rmdir(folder)

if __name__ == '__main__':
    if warn() == 0:
        move_from_subdirs()
        delete_subdirs()
