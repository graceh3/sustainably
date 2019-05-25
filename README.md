![Image](sustainably_cover1.png)

Recommend sustainable alternatives to popular fast-fashion handbags based on style and price similarities.
***
## Motivation



***
## Data Source & Methodology

__Data Source__
- [good on you](https://goodonyou.eco/) for sustainability ratings on fashion brands
- Web-scraped 1,500 images from 20 different brands using Selenium and BeautifulSoup

__Methodology__<br>


***
## Modeling

__VGG16__


***
## Results

With our baseline model,




***
## Takeaways

The out-of-the-box pretained model did not sufficiently extract features unique to handbags to recommend the most similar handbags, as demonstrated in the results above.

## Next Steps
- scrape more bag images
- customize pre-trained models (VGG16 and/or RESNET50) by freezing lower layers and training upper layers with bag images to have model predict different bag types (shoulder bag, tote bag, clutch, backpack, bum bag); extract features from this model to calculate minkowski distances
