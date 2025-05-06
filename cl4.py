def map_function(student_scores):
    for student_id,score in student_scores:
        yield student_id,score
def reduce_function(mapped_data):
    grades={}
    for student_id,score in mapped_data:
        if score>80:
            grade='A'
        elif score>60:
            grade='B'
        elif score>40:
            grade='C'
        else:
            grade='D'
        grades[student_id]=grade
    return grades
def map_reduce(student_scores):
    mapped_data=list(map_function(student_scores))
    grades=reduce_function(mapped_data)
    return grades
student_scores=[
    (1,800),
    (2,7),
    (3,45)
]

grades=map_reduce(student_scores)
for student_id,grade in grades.items():
    print(f"Student {student_id} has scored {grade}")

###################
def map_reduce(file_path,target_word):
    word_count=0
    with open(file_path,'r') as file:
        mapped_data=[(word.lower(),1) for line in file for word in line.strip().split()] #splits sentences into words and removes trailing and leading whitespaces
    
    for word,count in mapped_data:
        if word==target_word.lower():
            word_count+=count
    return word_count
file_path='test.txt'
target_word='start'
frequency=map_reduce(file_path,target_word)
print(f"The word {target_word} appears {frequency} times")


#################3


#Practical 5 KMeans Clustering

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris=load_iris()
X=iris.data

kmeans=KMeans(n_clusters=3)
kmeans.fit(X)

centroids=kmeans.cluster_centers_
labels=kmeans.labels_

plt.scatter(X[:,0],X[:,1],c=labels,cmap='viridis')
plt.scatter(centroids[:,0],centroids[:,1],marker='X',s=200,c='red')
plt.title("Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()



####################









#Practical 4 KNN CLassification

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

iris=load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)
k=5
knn=KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train_scaled,y_train)
y_pred=knn.predict(X_test_scaled)
acc=accuracy_score(y_test,y_pred)
acc

##################





import pandas as pd 
def map_reduce_with_pandas(input_file): 
    # Load the dataset 
    df = pd.read_csv(input_file) 
     
    # Map: Filter deceased males and transform data for average age calculation 
    deceased_males = df[(df['Survived'] == 0) & (df['Sex'] == 'male')] 
     
    # Reduce: Calculate average age of deceased males 
    average_age_deceased_males = deceased_males['Age'].mean() 
     
    # Map: Filter deceased females and transform data for count by class 
    deceased_females_by_class = df[(df['Survived'] == 0) & (df['Sex'] == 'female')] 
 
    # Reduce: Count deceased females by class 
    count_deceased_females_by_class = deceased_females_by_class['Pclass'].value_counts() 
    return average_age_deceased_males, count_deceased_females_by_class 
 
# Example usage 
input_file = 'Titanic-Dataset.csv'  # Update this to the path of your Titanic dataset CSV file 
average_age, female_class_count = map_reduce_with_pandas(input_file) 
print(f"Average age of males who died: {average_age:.2f}") 
print("Number of deceased females in each class:") 
print(female_class_count)


####################


from collections import defaultdict

# Read and parse the file
def read_scores_from_file(file_path):
    student_scores = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                name, score = parts[0], int(parts[1])
                student_scores.append((name, score))
    return student_scores

# Map function
def map_function(student_scores):
    grouped_scores = defaultdict(list)
    for name, score in student_scores:
        grouped_scores[name].append(score)
    return grouped_scores

# Reduce function
def reduce_function(grouped_scores):
    grades = {}
    for name, scores in grouped_scores.items():
        avg = sum(scores) / len(scores)
        if avg > 80:
            grade = 'A'
        elif avg > 60:
            grade = 'B'
        elif avg > 40:
            grade = 'C'
        else:
            grade = 'D'
        grades[name] = grade
    return grades

# Main map-reduce function
def map_reduce(file_path):
    student_scores = read_scores_from_file(file_path)
    mapped_data = map_function(student_scores)
    grades = reduce_function(mapped_data)
    return grades

# Run the program
file_path = 'scores.txt'  # Replace with your actual file path
grades = map_reduce(file_path)

for name, grade in grades.items():
    print(f"{name} has been assigned grade {grade}")
