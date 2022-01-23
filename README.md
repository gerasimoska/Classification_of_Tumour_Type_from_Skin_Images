# Classification of tumour type from skin images by using deep learning

## Data
The International Skin Imaging Collaboration: Melanoma Project is an academia and industry partnership designed to facilitate the application of digital skin imaging to help reduce melanoma mortality. <br>
The dataset contains total amount of 23906 images, which are separated in two classes for their diagnostic attributes accordingly to their metadata: benign or malignant.<br>
For each record in the dataset there are two files. The first one is in .json format, containing id, metadata (benign_malignant, age_approx, sex, diagnosis, diagnosis_confirm_type, anatom_site_general, melanocytic) and technical information about the image. The second one is the skin image in .tiff or .jpg format, in quite good resolution.<br>
The working dataset which is used in this project contains 496 skin images classified as benign tumour and 2123 skin images classified as malignant, from which after removing low quality photos 877 are used.<br>
The dataset is available on [ISIC Gallery](https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery)

## Preprocessing

The downloaded dataset contains all the files in a single folder without any separation by classes. With a simple Python function(datasetSeparation.py) all the files are separated according to the class(benign or malignant tumour) which is taken from the corresponding .json file and placed in the appropriate folder.<br>
For each image in the dataset, by using the Python script feature_extraction.py, 64x64 features are extracted. The numerical values are saved in .csv files, named featuresB.csv and featuresM.csv, each for the images of the appropriate type of tumour.<br>
Afterwards all the data is stored in features.csv where the first column represents the class (0 for Benign tumour, and 1 for Malignant tumour). The rest of the columns in each row represent the 4096 **features extracted**, and each row is data for one image of the dataset.

## ML model

Python’s [sklearn](https://scikit-learn.org/stable/) module is used for the model for predicting the image class (Benign or Malignant). The **Neural Network** receives numerical values as an input. Since there are 4096 features extracted for each image of the dataset, the first input layer of the ANN has 4096 nodes.<br>
The rest of the NN parameters which are used are the default ones, meaning one input layer, one hidden layer with 100 units and one output layer in the ANN, maximum number of iterations is 200, activation function for the hidden layer is ‘relu’ - the rectified linear unit function, returns f(x) = max(0, x). The output is the instance’s class (binary: 0/1 – B/M).<br>
The dataset is randomly separated into training and testing dataset, by using the module’s train_test_split function, which splits arrays or matrices into random train and test subsets. The size of the test dataset is 20%.<br>
Accuracy is calculated using the module’s accuracy_score function which returns the accuracy **classification score**. In classification, this function computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true. In binary and multiclass classification, this function is equal to the jaccard_similarity_score function.<br>
Since the dataset which is used for training and testing is not very large, there are multiple epochs of training and testing the ANN, and at the end the average accuracy of all the epochs is calculated. The number of epochs is a hundred, and the obtained average accuracy is 94%.

## POSSIBLE IMPROVEMENTS

Beside the quite satisfying results obtained with this model, there is always place for improvements. Some of the things which it can be worked on are:
- Increasing the dataset size
- Improving the feature extraction function
- Choosing bigger N as number of features to be extracted from each image in the dataset
- More hidden layers in the Neural Network
- Fine tuning the Neural Network’s parameters