from flask import Flask, render_template, url_for, request, redirect
import pickle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model


model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

dataset = pd.read_csv('Covid-data.csv', sep=',')
dataset = dataset.iloc[40796:41310, 2:5]
id = []
for i in range(1, len(dataset["location"]) + 1):
    id.append(i)
dataset.insert(2, "id", id, True)
x = np.array(dataset['id']).reshape(-1, 1)
y = np.array(dataset['total_cases']).reshape(-1, 1)
polyFeat = PolynomialFeatures(degree=10)
x = polyFeat.fit_transform(x)
known_cases = model.predict(x)

@app.route('/')
def index():
        return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    data = request.form['a']
    arr = np.array([[514 + int(data)]])
    polyFeat = PolynomialFeatures(degree=10)
    pred = model.predict(polyFeat.fit_transform(arr))
    createImage(int(data))
    return render_template('after.html', value=int(pred))

def createImage(data):
    days = data
    future_dates = np.array(list(range(1, 514 + days))).reshape(-1, 1)
    predicted_cases = model.predict(polyFeat.fit_transform(future_dates))
    req_date = np.array([514 + days]).reshape(-1, 1)
    plt.plot(predicted_cases, color='red', ls='-')
    plt.plot(known_cases, color='blue', ls='-')
    yd = model.predict(polyFeat.fit_transform(req_date))
    plt.scatter(req_date, yd, color="black")
    plt.title("Total Covid Cases Vs Days")
    plt.xlabel("Number of Days")
    plt.ylabel("Total Cases")
    plt.legend(["Predicted Cases", "Observed Cases", "Requested Day"], loc="upper left")
    fig1 = plt.gcf()
    fig1.savefig('static\images\graph.png', dpi=100)
    plt.close(fig1)


if __name__ == "__main__":
    app.run(debug=True)

