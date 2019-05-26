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

Below are some of the results of the top 3 most similar ethical bags for a particular unethical bag. The model seems to be able to discern some high-level shapes and saturation but fails to accurate recommend the same bag type and finer details like color and texture.

<p align='center'>
 <img width="600" alt="results1" height="220" src="images/results1.png">
</p>

<p align='center'>
 <img width="600" alt="results2" height="220" src="images/results2.png">
</p>

<p align='center'>
 <img width="600" alt="results3" height="220" src="images/results3.png">
</p>

<p align='center'>
 <img width="600" alt="results4" height="220" src="images/results4.png">
</p>

***
## Takeaways

The out-of-the-box pre-trained model did not sufficiently extract features unique to handbags to recommend the most similar handbags, as demonstrated in the results above.

## Next Steps
- scrape more bag images from other ethical sources (like consignment shops that recycle used products) as well as sustainable brands that create new project (like nanushka)
- customize pre-trained models (VGG16 and/or RESNET50) by freezing lower layers and training upper layers with bag images to have model predict different bag types (shoulder bag, tote bag, clutch, backpack, bum bag); extract features from this model to calculate minkowski distances
- down the line, expand product line to include shoes, then clothing
