# Who's that BTS Member?

This is a mini facial recognition project using the in-built classifiers and recognisers in OpenCV that attempts to recognise BTS members from images.

This project is composed of a few steps:

1. An automated system to obtain training data in the form of images.

   - This step explores the usage of **Selenium** and the **scikit-image** library.
   - It also uses OpenCV to pre-detect faces in the image and takes in user input to validate whether the images should be saved.

2. Process the images and train the model.
   - This step converts the images to grayscale, crops the images to the region of images (ROI) and labels them.
   - These ROI and labels are then used to train a model using the LBPH algorithm.
   - Uses the LBPHFaceRecognizer in OpenCV.
3. A face detection system that applies the recogniser to mark and label the faces.
   - Detects the face in the validation image, gets the ROI and predict a label.
   - Draw the rectangle and write the prediction on the image.

## 1. Obtaining the Training Data

Any machine learning project requires data, and a whole lot of it.

### References

1. https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59
2. https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/

## 2. Train the Model

### References

1. https://www.superdatascience.com/blogs/opencv-face-recognition
2. https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b
3. https://machinelearningmastery.com/difference-between-algorithm-and-model-in-machine-learning/
4. https://docs.opencv.org/master/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html
