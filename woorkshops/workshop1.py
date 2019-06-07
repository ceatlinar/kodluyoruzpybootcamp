from os import listdir
import os
from os.path import isfile, join
mypath = 'C:\\Users\\atlin\\Desktop\\b'
dirName = mypath + '\\gifs'

def read_all_files(mypath):
    return  [f for f in listdir(mypath) if isfile(join(mypath, f))]


def split_images(images):
    counter = 0
    for img in range(len(images)):
        if images[img].endswith('.gif'):
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            os.rename(mypath + '\\' + images[img],dirName + '\\' + str(counter).zfill(5) + '.gif')    
            counter += 1
        else:
            os.rename(mypath + '\\' + images[img],mypath + '\\' + str(counter).zfill(5) + '.jpg')
            counter += 1

images = read_all_files(mypath)
split_images(images)
