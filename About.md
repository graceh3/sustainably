When it comes to shopping, fast fashion has become the norm even though many of us are becoming aware of the negative implications of supporting companies that practice this type of production. Over the years, we’ve seen a growth of sustainable options, but not everyone has the time, or patience to shop around for the perfect piece. 

This is where GoodTwin comes in.  We decided the best way to help people be more responsible is to make being responsible the easy option. What our model allows you to do is input an image of a bag that you love and recommend very similar bags that are a more sustainable option. Currently, our model only supports bags on white backgrounds, however in the next months we plan to improve our model to be background-agnostic and eventually broaden our scope to other product categories, such as clothing and shoes to provide a full, sustainable shopping experience. 

In the following pages we will discuss four aspects of the project and our development process.

Determining the ethicality of brands
Scraping data
Choosing and developing a model
Breaking down the results 
Next steps

1. Determining the ethicality of brands
The first step in the process was to make sure that we knew how to accurately identify brands that truly followed ethical practices. This was challenging given the pervasiveness of greenwash marketing aimed at appealing to consumers’ growing desire to make environmentally responsible choices. So, for this purpose, we outsourced the research and collection to the website Good On You. This page is dedicated to determining how ethical brands are, and it made it really clear pretty quickly that the brands we assumed were ethical were not. If you want to read more about how they determine how ethical a brand is, look here. In addition to Good On You, we also sourced bags from second-hand retailers like ThredUp and Rebag - even if the bags themselves were not made ethically, buying items that have already been created (and otherwise would have been disposed) is a solid, sustainable option.

2. Scraping data
After gathering a list of brands and companies, we got to work scraping bag images and their related data. We knew that a well-trained model would require at least a few thousand images, so we decided to scrape as many images as possible. You can view our scraping scripts in our GitHub repo here (we used a combination of requests, Selenium, and BeautifulSoup).

One big factor that narrowed down our options for brands was the quality and styling of their images. For our current model, we require images that have plain backgrounds. Until we update our model in the next few months, the backgrounds are a confounding factor for the neural net. Instead of only focusing on the bags themselves they begin to start using the background as features of the bag themselves.

As you will see in the scripts, to download images from a link using selenium you will also need to use multiple other libraries that are image specific: urllib, Image from PIL, and BytesIO from io, requests. An example of this process looks like this:

#c is the count of which image for this company your on

response = requests.get(url)
img = Image.open(BytesIO(response.content))
image_save_loc = 'folder_to_save/'+'company_'+str(c)+'.jpg'        img.save(image_save_loc, "JPEG")

After scraping about 8,000 bags and their images we were ready for the development process.

3. Choosing and Developing a Model

Now that we had our data, we needed to choose an approach to building our model. The two main choices that we had were building a CNN from scratch or using a pretrained model from the Keras library. We wanted the most accurate results possible so we opted to experiment with VGG16 and ResNET50 using ImageNet weights, a common practice in deep learning. Pretrained models are essentially out-of-the-box deep learning models that have already gone through an extensive training process on tens of thousands of images.

With these pretrained models, you can customize the model to solve various image-based classification problem.. In addition, and as is common practice with image data, you can extract features of each image based on the final values of the outermost dense layer produced by the model. This feature matrix represents how the model ‘sees’ each image. Once you have the feature matrix, you choose a spatial distance calculation metric to determine how close in similarity each image is from one another. 

As a baseline attempt, we ran all images through the standard VGG16 model and extracted the features from its outermost dense layer. We then created a cosine similarity matrix of all the images and observed the output of the top 10 most ‘similar’ images to determine how well our model performed. Some of the results that we saw are below. As you can see, using the VGG16 model as-is did not produce the level of similarity that we wanted to see. \

One of the most basic issues that we knew we needed to correct for was making sure that we recommend the same type of bag (tote/shoulder/clutch) as the input bag. When someone is shopping for a backpack, the chances are that they want to see other backpacks, not other totes or weekenders. This observation told us that we needed to customize our model.

At a baseline, we wanted to absolutely make sure that we were categorizing the same bag types together, so we knew we needed to select our bag type groups and train the model to classify the right bags together. Once that’s done, we would end up with feature matrices that would naturally group the same bag types together, in addition to picking up on other characteristics such as color, pattern, and shape. 

Since the images used to generate the ImageNet weights are pretty different, we decided to freeze the bottom layers of the model, retrain the top four layers, and add one dense layer and a final softmax layer to output our eight bag classes. 

After making these changes, our results improved dramatically. Below are some sample outputs of the model. While there are still some errors, we saw better matches with the classes, shapes, and colors.





-------------------------------------------------------------------------------------------------------------------------------


To accomplish what we needed to do we first cut off the last few layers of the model, and created the number of end nodes to match the number of classes we had for our bags (8). For this, we went with a process that is commonly referred to as fine tuning a CNN. This means we froze many of the lower layers of our model before retraining the top layers on our images. The number of layers we froze was varied to determine our best option. After numerous trials, the VGG16 stood out as a more effective model for our task.

So, after hypertuning our model more, adding and removing different layers to the end, and reaching a training accuracy of ____, we then extracted the final dense layer to get image features matrices. Simply, these matrices represent what the model sees in each image. They allow us to determine how similar bags are to each other. As mentioned previously, we used bags without a background. When you begin to look at the features created by the CNN you realize how the model’s layers are “viewing” each image. 

With one of the first models, due to the way we separated images it was distracted by the straps of the bags and the texture of the fabrics used. In other types of models, these would be features that the model is interpreting as having bigger causality for what you’re predicting for. And in this case, it’s exactly the same, it thought that handles were more indicative than other features--meaning handles had higher feature importance than other features like shape.  

However, after adding the correct number of categories and training on a sufficient number of images we were able to have the VGG16 model focus on what was most important to us: the type of bag and the color/patterns of that bag. Examples of what we’ve seen can be seen here:

4. Breaking down the results 

After our model was ready and we created feature matrices for all of our ethical bags we were ready to make predictions. For this kind of problem, unlike separating the images into categories, there was no way to objectively say the matches were correct or not. So, we moved forward using cosine similarity for our 










***


1. Motivation
When it comes to shopping, fast fashion has become the norm.  However, consumers today are becoming aware of the negative impact the fast-fashion industry has not only on the environment but on their workforce as well.  Over the years, we’ve seen a growth of sustainable options, but not everyone has the time nor the patience to conduct their own research and shop around for the perfect piece. 

This is where GoodTwin comes in.  We decided the best way to help people be more responsible is to make being responsible the easy option. 
We built a neural-network-based recommendation system that takes in an image of a bag that a user loves and outputs sustainable alteratives that are similar in style and design.  With our platform, we hope to make sustainable shopping the go-to choice for everyone and in turn push the fashion industry to do better by the environment and their people.

While our beta concept works only on bags, we plan to expand into other product categories such as shoes and clothings in the near future.

2. Plan 
(a) Research ethical brands - we relied on the robust rating system of Good On You to determine which ethical brands to recommend. They've rated over 2k brands on dimensions aroud how companies treat their workers, the environment, and animals.
(c) Get data - 
(d) Train the model - we worked with a deep-learning model to extract image features
(e) Determine a similarity metric - 
(f) Design website & deploy model - 

3. Our Results

4. Our Next Steps
- Deconstruct some of the bag categories into more granular groups for better feature extraction.
- Background-agnostic image recognition .
- Include price as a dimension in recommendation, either as a filter or sort feature as a layer above the results.












Pagination video: https://www.youtube.com/watch?v=lOcLr6CXg2s