import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA

df = np.array(pd.read_csv("./ParisHousing.csv", header=0).values)
X = df[:, :16]
Y = df[:, 16]

#print(X)
#print(Y)
min = 0.0000000000000001
max = 0

BestLinear = 0
BestPCA = 0
num_pca = 0

X_train, X_valid, Y_train, Y_valid = 0,0,0,0

def predict(sqrt, nOR, hY, hP, flr, cD, cPR, nPO, made, iNB, hSP,basem, attic, gara, hSR, hGR):
    sample_test = [[sqrt, nOR, hY, hP, flr, cD, cPR, nPO, made, iNB, hSP, basem, attic, gara, hSR, hGR]]
    print(sample_test);
    price = BestLinear.predict(BestPCA.transform(sample_test))
    return price


for j in range(1, 8):
    print("Lan:", j)
    modelPCA = PCA(n_components=j).fit(X)
    print(modelPCA)

    X_new = modelPCA.transform(X)  # Dùng để giảm size cho X
    # giảm size cho X


    X_train, X_valid, Y_train, Y_valid = train_test_split(X_new, Y, test_size=0.3, random_state=0)

    modelLinear = LinearRegression().fit(X_train, Y_train)
    y_pred = modelLinear.predict(X_valid)

    d = 0
    sum = 0

    for i in range(len(y_pred)):
        sum += (abs(y_pred[i] - Y_valid[i]))

    mean = sum / len(y_pred)

    for i in range(len(y_pred)):
        if (abs(y_pred[i] - Y_valid[i]) < mean) :
            d += 1

    rate = d / len(y_pred)

    print("Classification Accuracy:", rate, "\n")

    if (rate > max):
        num_pca = j
        BestPCA = modelPCA
        max = rate
        BestLinear = modelLinear

print("Max:", max, "d=", num_pca)
#
print("Thực tế \t\t Dự đoán" )
for i in range (0, 8):
    print( Y_valid[i],"\t\t",  y_pred[i])