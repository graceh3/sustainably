import time
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import numpy as np

c = 0
def save_src_image_apply(path,short,url):
    '''
    This function will either download the image at the url or 
    return the error message. The filename or error message 
    will be stored in the DataFrame.
    -------------------------------------
    Parameters/input:
    path: the file path of the folder where the image will be saved.
    short: the "short" name for the company, beg. of the file name
    url: url of image from the DataFrame
    -------------------------------------
    Output:
    e: error message if file cannot be downloaded
    short_c.png: file name of downloaded img
    '''
    slp = numpy.random.randint(1,10,size=1)
    time.sleep(slp[0])
    global c
    try:
        c += 1
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        image_save_loc = company+short+'_'+str(c)+'.png'
        img.save(image_save_loc, "PNG")
        print("Saved "+short+"_{}".format(c)+".png")
        return short+"_"+ str(c)+".png"
    except Exception as e:
        return e
    
    
def subdir_len(path):
    '''
    Function returns the number of itmes in each subdiretory
    of the main directory provided as a parameter.
    Parameters: 
    -----------------------------------
    path: path to the folder being inspected
    Output: 
    -----------------------------------
    len(os.listdir(..)): Number of items in current subdir.
    folder: name of above folder
    '''
    # get all directories 
    folders = ([name for name in os.listdir(path) if name != '.DS_Store']) 
    
    #print item count, followed by folder name
    for folder in folders:
        print(len(os.listdir(os.path.join(path,folder))),folder)