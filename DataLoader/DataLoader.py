from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from Constants import DATA_SET_FULL_PATH
import numpy as np
import pandas as pd
import os

def load_data_from_csv():
    file_path = DATA_SET_FULL_PATH

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        print(f"File '{file_path}' does not exist. Check the file path.")

    features_letters = df.values[:, 1:]
    labels_letters = df.values[:, 0]

    features_letters = features_letters.reshape(len(features_letters), 28, 28, 1).astype('float32')
    features_letters /= 255

    return features_letters, labels_letters


def load_mnist_data():
    (X_train_mnist, y_train_mnist), (X_test_mnist, y_test_mnist) = mnist.load_data()

    X_train_mnist = X_train_mnist.reshape(60000, 28, 28, 1).astype('float32') / 255
    X_test_mnist = X_test_mnist.reshape(10000, 28, 28, 1).astype('float32') / 255

    return X_train_mnist, y_train_mnist, X_test_mnist, y_test_mnist


def combine_datasets(features_letters, labels_letters, X_train_mnist, y_train_mnist):
    combined_features = np.concatenate((features_letters, X_train_mnist), axis=0)

    labels_letters += 10
    combined_labels = np.concatenate((labels_letters, y_train_mnist), axis=0)

    n_classes = 36
    combined_labels = to_categorical(combined_labels, n_classes)

    return combined_features, combined_labels


def split_data(combined_features, combined_labels):
    X_train, X_test, y_train, y_test = train_test_split(combined_features, combined_labels, test_size=100000,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test
