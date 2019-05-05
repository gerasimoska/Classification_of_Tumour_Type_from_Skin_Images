import spicy
import cv2
import numpy as np
from imageio import imread

# Feature extractor
def extract_features(image_path, vector_size=64):
    image = imread(image_path)
    try:
        # Using KAZE, cause SIFT, ORB and other was moved to additional module
        # which is adding addtional pain during install
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them.
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print('Error: ', e)
        return None

    return dsc


imagesB=[]
imagesM=[]

for i in range(0, 36066):
    try:
        imgFileName="ISIC-images\\benign\\ISIC_00"+str(i).zfill(5)+".jpg"
        imagesB.append(imgFileName)
    except Exception as e:
        try:
            imgFileName = "ISIC-images\\malignant\\ISIC_00" + str(i).zfill(5) + ".jpg"
            imagesM.append(imgFileName)
        except Exception as e:
            pass

imagesB_features=[]
imagesM_features=[]

fB = open('featuresB.csv','w')
for image in imagesB:
    try:
        e=extract_features(image)
        imagesB_features.append(e)
        print(e)
        fB.write("0,"+e+"\n")
    except Exception as ex:
        pass
fB.close()

fM = open('featuresM.csv','w')
for image in imagesM:
    try:
        e=extract_features(image)
        imagesM_features.append(e)
        print(e)
        fM.write("1,"+e+"\n")
    except Exception as ex:
        pass
fM.close()