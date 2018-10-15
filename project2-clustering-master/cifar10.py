import pickle
import numpy as np
import matplotlib.pyplot as plt
import util

def load_data(fp):
    '''
    Tuple of array and labels representing CIFAR10 Data
    '''

    X, y = None, None
    # TODO: write code to unpickle stored dictionary of data and labels
    #util.raiseNotDefined()
    
    with open(fp, 'rb') as fo:
        datadict = pickle.load(fo, encoding = 'latin1')
        
    
    X = datadict['X']
    y = datadict['y']
    
    X = X.astype(np.int)
    
    y = np.array(y)
    
    assert(X.dtype == np.int)
    assert(y.dtype == np.int)
    return (X, y)

def normalize_img(X):
    '''
    return the image with values scaled to between [0, 1]
    '''
    # TODO: Your code here
    img = X.copy()
    for val in img:
        print(val)
        val = val/255
    return img

def show_img(X, normalize=False):
    '''
    Display given image
    '''
    img = X.copy()
    img = img.reshape(3,16,16).transpose([1, 2, 0])
    if normalize:
        img = normalize_img(img)
    plt.imshow(img)
    plt.show()

def show_imgs(X, labels=None, normalize=False):
    '''
    Display given list of images and label images with given list of
    labels (if supplied)
    '''
    assert(len(X <= 64))
    labels = labels if labels is not None else range(len(X))

    assert(len(X) == len(labels))

    imgs = X.copy()
    imgs = imgs.reshape(-1,3,16,16).transpose([0,2, 3, 1])
    plt.figure(figsize = (10,10))
    for i, img in enumerate(imgs):
        if normalize:
            img = normalize_img(img)
        plt.subplot(8, 8, i+1)
        plt.imshow(img)
        plt.text(0,6,str(labels[i]), color='blue')
    plt.show()
