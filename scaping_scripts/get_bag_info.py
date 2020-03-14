# helper function to get bag info and locally save bag images

import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
import requests
import urllib.request


def get_bag_info(url, bag_type, img_directory, counter_start, is_ethical, source):
    '''
    PARAMETERS
    ----------
    - url : str format of page url
    - bag_type : str format of bag type
    - img_directory : str format of local directory for saved images
    - counter_start : int counter start value for file naming convention
    - is_ethical : int/boolean whether source is ethical or not
    - source : str format of website source

    OUTPUT
    ----------
    - dataframe containing bag details
    - dictionary containing bag details
    - images saved locally to specified img_directory
    '''
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')

    # find all bag data in html for given url
    bags = soup.find_all('div', {'class': 'carousel-results-item item-card listed'})

    # initiate lists of data to acquire
    bag_names = []
    bag_brands = []
    bag_prices = []
    bag_urls = []
    bag_image_urls = []
    bag_img_fnames = []

    # loop through class tags to get each bag info
    for i, b in enumerate(bags):
        bag_names.append(b.find('div', {'class': 'item-title'}).text)
        bag_brands.append(b.find('div', {'role': 'link'}).text)
        bag_prices.append(b.find('div', {'class': 'formatted-prices'}).text)
        bag_urls.append(f'https://www.thredup.com'+b.find('a').attrs['href'])

    # go into each bag url and get large bag image url
    print(f'Getting bag image URLs')
    for i, url in enumerate(bag_urls):
        print(f'{i+1}/{len(bag_urls)}')
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        for img in soup.findAll('img'):
            if 'large' in img.attrs['src']:
                bag_image_urls.append(img.attrs['src'])
        time.sleep(0.25)

    # format bag data into a dictionary
    all_data = {'name': bag_names,
                'brand': bag_brands,
                'price': bag_prices,
                'bag_url': bag_urls,
                'img_filename': bag_img_fnames}

    # make sure you have same number of image urls and bag names
    if len(bag_image_urls) == len(bag_names):
        # save bag images to local direcotry
        print(f'Saving images to {img_directory}.')
        for i, url in enumerate(bag_image_urls):
            brandname = bag_brands[i].strip().replace(' ', '')[:3].lower()
            fname = f'thredup_{brandname}_{counter_start+i}.png'
            file_name = f'{img_directory}/{fname}'
            urllib.request.urlretrieve(url, file_name)
            bag_img_fnames.append(fname)

        # convert dictionary to dataframe
        df = pd.DataFrame(all_data)
        df['label'] = bag_type  # adding bag type to all items in dataframe
        df['is_ethical'] = is_ethical  # boolean value (1 = yes, 0 = no)
        df['source'] = source

        print(f'Bag images have been saved to {img_directory}.')
        return df, all_data
    else:
        return None
