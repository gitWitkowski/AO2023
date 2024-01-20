import cv2
import numpy as np


def load_and_process_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is not None:
        threshold_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda c: cv2.boundingRect(c)[0])

        cropped_chars = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            char = threshold_img[y:y + h, x:x + w]
            char = cv2.resize(char, (28, 28))
            char = char.astype('float32') / 255
            char = char.reshape(1, 28, 28, 1)
            cropped_chars.append(char)

        return cropped_chars
    else:
        print("Image not loaded.")
        return None


def predict_text_from_image(cropped_chars, model):
    if cropped_chars is not None:
        predicted_string = []

        for char in cropped_chars:
            y_prediction = model.predict(char)
            predicted_class = np.argmax(y_prediction)

            if predicted_class > 9:
                predicted_char = chr(ord('A') + predicted_class - 10)
            else:
                predicted_char = str(predicted_class)

            predicted_string.append(predicted_char)

        final_string = ''.join(predicted_string)
        print("Predicted String:", final_string)
        return final_string
    else:
        return None
