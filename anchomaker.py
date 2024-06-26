import numpy as np
import glob
import os
from sklearn.cluster import KMeans

# Path to the current directory with annotation files
current_dir = './'

# Function to load dataset annotations
def load_dataset(path):
    dataset = []
    for file in glob.glob(path):
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                if len(parts) == 6:  # Ensure the line has the correct format
                    width = float(parts[3]) * 640  # Calculate width in pixels
                    height = float(parts[4]) * 512  # Calculate height in pixels
                    dataset.append([width, height])
    return np.array(dataset)

# Load dataset from current directory
annotation_path = os.path.join(current_dir, '*.txt')
dataset = load_dataset(annotation_path)

# Check if dataset is empty
if len(dataset) == 0:
    print("No annotation files found or they do not match the expected format.")
    print("Make sure your annotation files are in the current directory and in the correct format.")
    exit()

# Set the number of clusters (should be the same as the original number of anchors)
num_clusters = 9

# Check if number of clusters is greater than the number of data points
if num_clusters > len(dataset):
    print("Number of clusters cannot be greater than the number of data points.")
    print("Reduce the number of clusters or ensure sufficient annotation data.")
    exit()

# Run K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(dataset)
anchors = kmeans.cluster_centers_

# Sort anchors for better organization
anchors = anchors[np.argsort(anchors[:, 0] * anchors[:, 1])]

# Reshape anchors to fit YOLOv5 format
anchors = anchors.reshape(3, 3, 2)

print("New anchors:")
print(anchors)
