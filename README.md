# BTS Recogniser using OpenCV

This is a mini facial recognition project using the in-built classifiers and recognisers in OpenCV that attempts to recognise BTS members from images.

The idea for this project came as a joke when a friend asked to name BTS members from an image and I threatened to create a recogniser to do the job for me. Despite being a joke, I realised this would be a fun project to bring to life while simultaneously learning computer vision.

Breaking down the project into its components, I needed a few things:

1. An automated system to obtain training data (Search and download a relatively large number of images for training)
2. Processing the images and labeling them to train the recogniser.
3. A face detection system that applies the recogniser to mark and label the faces.

## 1. Obtaining the Training Data

Any machine learning project requires data, and a whole lot of it.

### References

1. https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59
2. https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/

## 2. Train the Model

### References

1. https://www.superdatascience.com/blogs/opencv-face-recognition
2. https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b
