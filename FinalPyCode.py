import serial
import time
from keras.models import load_model
import cv2
import numpy as np

# Initialize Serial Communication
serial_port = "COM5"
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate)
ser.close()
time.sleep(1)
ser.open()

# Load the model and labels
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

# Initialize Camera
camera = cv2.VideoCapture(0)

while True:
    # Image Recognition Process
    ret, image = camera.read()
    image = cv2.flip(image, 1)
    
    # Get image dimensions
    height, width, _ = image.shape

    # Calculate crop size and coordinates
    crop_width = 720
    crop_height = 720
    center_x = width // 2
    center_y = height // 2
    start_x = center_x - crop_width // 2
    start_y = center_y - crop_height // 2
    end_x = start_x + crop_width
    end_y = start_y + crop_height

    # Crop and resize the image
    cropped_image = image[start_y:end_y, start_x:end_x]
    image = cv2.resize(cropped_image, (224, 224))

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Prepare the image for prediction
    image_array = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image_array = (image_array / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image_array)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print(f"Class: {class_name[2:]}, Confidence Score: {np.round(confidence_score * 100)}%")

    # Send Data to Serial Port
    ser.write(f"{class_name[2:]}\n".encode())

    # Break the loop with 'q' key
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()
ser.close()
