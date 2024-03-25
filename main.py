import pandas as pd
import numpy as np
import math

# Read the uploaded CSV file
data = pd.read_csv('test.csv')

#eucledian distance between two points
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#average linkage between two clusters
def average_linkage(cluster1, cluster2):
    distances = []
    for point1 in cluster1:
        for point2 in cluster2:
            distances.append(euclidean_distance(point1[0], point1[1], point2[0], point2[1]))
    return np.mean(distances)

#average hierarchical clustering
def average_hierarchical_clustering(data):
    clusters = {row['label']: [(row['x'], row['y'])] for index, row in data.iterrows()}
    cluster_names = {label: label for label in clusters.keys()}
    step = 0

    while len(clusters) > 1:
        # Find the closest pair of clusters
        min_distance = float('inf')
        for label1, cluster1 in clusters.items():
            for label2, cluster2 in clusters.items():
                if label1 != label2:
                    # Calculate the average linkage between the two clusters
                    distance = average_linkage(cluster1, cluster2)
                    if distance < min_distance:
                        # Update the closest pair of clusters
                        min_distance = distance
                        # Update the closest pair of cluster labels
                        closest_pair = (label1, label2)

        cluster1, cluster2 = closest_pair
        step += 1
        print(f"Step {step}, we merge {cluster_names[cluster1]} and {cluster_names[cluster2]};")
        
        new_cluster_name = cluster_names[cluster1] + cluster_names[cluster2]
        for label in [cluster1, cluster2]:
            for k, v in cluster_names.items():
                if k == label or cluster_names[k] == cluster_names[label]:
                    cluster_names[k] = new_cluster_name
                else:
                    cluster_names[k] = v
        
        clusters[cluster1] += clusters.pop(cluster2)
    print("Done.")

clustering_steps_uploaded = average_hierarchical_clustering(data)
print("Please note that the letters order may not be the same as the mcq but the output is correct just the arrangement of letters maybe a little different")
