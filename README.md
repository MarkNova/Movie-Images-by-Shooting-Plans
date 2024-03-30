
# Movie Images by Shooting Plans

I have collected about **49.000 film footages**, each of which belongs to one of the seven classes depending on the shooting plan:

- Extreme Close Up
- Close Up
- Medium Close Up
- Medium
- Medium Wide
- Wide
- Extreme Wide


You can train your own frame classification model and use it in your own projects related to content analysis, metadata creation, automation of editing processes, etc. I hope this data will be useful for you ^_ . https://www.kaggle.com/datasets/minutcoff/movie-images-by-types-of-shooting-plans

I have saved several notebooks and python files in this repository. Some are useful for further data collection, in others I train the efficientnet_v2_s model and analyze model errors. 

During the study, it turned out to achieve an average **accuracy** of **0.7314**. At first glance, the result is not impressive, but I want to note that if you ask a person to solve this problem, they are likely to face great difficulties. Below you can see some of the images in which the model was mistaken during the validation process:

![alt text](errors_png\__results___7_0.png)



