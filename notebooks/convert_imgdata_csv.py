import csv
import os
import numpy as np
from PIL import Image

dir_path = "./data/interim/data3a/training/01-minor"
for root, dirs, files in os.walk(dir_path):

    # print(root, dirs, files)
    count = 0
    for file in files:
        file = file.lower()
        # print(file)
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            image_path = os.path.join(root, file)
            label = os.path.basename(root)

            # Load image
            image = Image.open(image_path)

            # Convert image to grayscale
            image = image.convert('L')

            # Convert image to numpy array
            image_array = np.array(image)

            # Flatten the array
            image_vector = image_array.flatten()

            new_array = np.append(image_vector, label)

            # Save the vector to a CSV file
            with open('/Users/rohitgulve/Documents/Applied_Machine_Learning/machine-learning-dse-i210-final-project'
                      '-damageseveritydetection/data/interim/image_data.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(new_array)
                count += 1
                print(f"added images {count}")
