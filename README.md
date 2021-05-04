# Who's that BTS Member?

This is a mini facial recognition project using the in-built classifiers and recognisers in OpenCV that attempts to recognise BTS members from images. This repository does not include the training and validation images that I used and hence this code could technically be modified to create a recogniser of other interest.

This project is composed of a few steps:

1. An automated system to obtain training data in the form of images. `image_scraper.py`

   - This step explores the usage of **Selenium** and the **scikit-image** library.
   - It also uses OpenCV to pre-detect faces in the image and takes in user input to validate whether the images should be saved.

2. Process the images and train the model. `trainer.py`
   - This step converts the images to grayscale, crops the images to the region of interest and labels them.
   - These regions and labels are then used to train a model using the LBPH algorithm.
   - Uses the LBPHFaceRecognizer in OpenCV.
3. A face detection system that applies the recogniser to mark and label the faces. `bts_recogniser.py`
   - Detects the face in the validation image, gets the ROI and predicts a label.
   - Draws the rectangle and write the prediction on the image.

### Updates

- 3/5/2021 - Trained an early stage model `faces_trained.yml` with 9 images for each member. Recognises certain members correctly but with very low confidence (eg. RM with 39%, honestly this is still better than me as a human)

<img src="https://user-images.githubusercontent.com/63803360/116885986-1f2d5c80-ac5b-11eb-9cda-100c200b8b7d.png" height=500>

- 4/5/2021 - Increased training data for certain members (planning to have more and equal number for all members) and trained a new model `bts_faced_trained.yml`. Accuracy of prediction improved but confidence remains low.

### References

- Automating the Search for Training Data

1. https://levelup.gitconnected.com/how-to-download-google-images-using-python-2021-82e69c637d59
2. https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/

- Learning How to Use the In-Built Recognizer in OpenCV with the LBPH Algorithm.

1. https://www.superdatascience.com/blogs/opencv-face-recognition
2. https://towardsdatascience.com/face-recognition-how-lbph-works-90ec258c3d6b
3. https://machinelearningmastery.com/difference-between-algorithm-and-model-in-machine-learning/
4. https://docs.opencv.org/master/df/d25/classcv_1_1face_1_1LBPHFaceRecognizer.html
