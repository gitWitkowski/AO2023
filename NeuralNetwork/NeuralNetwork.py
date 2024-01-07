import numpy as np
from matplotlib import pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten, BatchNormalization


def create_neural_network():
    model = Sequential()

    model.add(Conv2D(32, (3, 3), strides=(1, 1), activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(64, (3, 3), strides=(1, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))
    model.add(Conv2D(128, (3, 3), strides=(1, 1), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())
    model.add(Dropout(0.25))
    model.add(Flatten())

    model.add(Dense(256, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(128, activation='relu'))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(36, activation='softmax'))

    model.summary()
    return model


def configure_model(model):
    model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    return model


def train_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train, batch_size=128, epochs=10, verbose=1, validation_data=(X_test, y_test))
    return model


def evaluate_model(model, X_test, y_test):
    y_prediction = model.predict(X_test)
    y_prediction_classes = np.argmax(y_prediction, axis=1)
    y_test_classes = np.argmax(y_test, axis=1)

    zipped = zip(y_prediction_classes, y_test_classes)
    counter = 0

    for i, (predicted, actual) in enumerate(zipped):
        if predicted != actual:
            counter += 1
            plt.imshow(X_test[i], cmap='Greys')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
            print('Predicted value: ', predicted)
            print('True value: ', actual)

    print(counter)
