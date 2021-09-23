# GetPet-recognition
GetPet is an app for pet lovers.

This section covers the whole subject of machine learning in the app, dog and cat breed identification given a photo or video.

# Credits
- May Bachar
- Dana Kraimer
- Chen Baadani

# Usage
In the following link is the data for training the model for identifying dog breeds:

https://drive.google.com/drive/folders/1M7SxtGOPno9mGqIyhHxGHdq0ynPvm6-U?usp=sharing

labels file: https://drive.google.com/file/d/1-3Uf7ZwbNMKV6_DZEWIKcRV6dhHHxNcD/view?usp=sharing

In the following link is the data for training the model for identifying cat breeds:

https://drive.google.com/drive/folders/1Na3ectWz9-yEgyi9-_0tF_1q_lGcrU2L?usp=sharing

labels file: https://drive.google.com/file/d/1rW1JRb9XuQOWvizkV4zQe6FyPOCwujW0/view?usp=sharing

Now that you have the data and the labels file, you can run the file to train the dog or cat model. 
After training, Json and h5 files are obtained in which the weights are stored.
We will use these weights for the recognizer file which given an image returns a list of 3 breeds that the model 
predicted and the probability percentages for each breed in the list.
There is also the Flask server that receives image prediction requests or a sequence of images from video and returns a suitable prediction.
