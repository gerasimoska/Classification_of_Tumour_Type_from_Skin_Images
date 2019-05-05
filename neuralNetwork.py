import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

names=[]
names.append("class")
for i in range(1, 4097):
    names.append("feature"+str(i))

print(names)

data = pd.read_csv("features.csv", names=names)
results = open("Results_NeuralNetwork.txt","w")
result=0

avgAccuracy=0.0

for i in range(0,101):
  for cnt in range(0,888):
      X = data.drop(["class"], axis=1)
      y = data["class"]
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

  model = MLPClassifier()

  print("\n\nGOAL:")
  print(y_test)
  results.write("GOAL:"+"\n"+str(y_test) + "\n")

  model.max_iter=2000
  model.fit(X_train, y_train)

  #print(accuracy_score(y_train, model.predict(X_train)))
  print("\n\nPREDICTED:")
  print(model.predict(X_test))
  print("Accuracy: "+str( accuracy_score (y_test, model.predict(X_test))) )
  results.write("PREDICTED:"+"\n"+str(model.predict(X_test)) + "\n\n\n")
  avgAccuracy += accuracy_score(y_test, model.predict(X_test))

print("Average accuracy is: "+str(avgAccuracy))
results.write("Accuracy is: "+str(avgAccuracy))