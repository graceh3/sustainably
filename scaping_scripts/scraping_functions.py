import time
from PIL import Image
import requests
from io import BytesIO
import pandas as pd

c = 0
def save_src_image_apply(company,short,url):
    time.sleep(1)
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