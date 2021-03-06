# FishNet
FishNet: a mimic of FaceNet with fish image as input.

## How to Install and Run
1. Download the pretrained ResNet-50 fish classifier model from [here](https://drive.google.com/open?id=1ouJ8xZzi6x2cEkojS3DC1Wy77zjBGP1c)
2. Create Virtual Environment with Conda
```
$ conda create -n FishNet python=3.6 pip
$ conda activate FishNet
$ pip install -r requirements.txt
```
3. Run the [classification with SVM](notebook/demo-svm.ipynb) demo (be sure to start ```jupyter notebook```!!!)

## Demo
1. [classification with SVM](notebook/demo-svm.ipynb)
2. [fish vector calculation](notebook/demo-images.ipynb)

## Reference
1. FaceNet
    - https://github.com/davidsandberg/facenet
    - This repo gives me the concept of FaceNet.
2. Keras FaceNet
    - https://github.com/nyoki-mtl/keras-facenet
    - Classification with SVM and fish vector calculation demo originates from here.
