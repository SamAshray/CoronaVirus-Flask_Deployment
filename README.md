This project is a Deployed version of an earlier prediction model (Corona Predictor) using Flask Web Framework.

This contains data mining, data pre-processing and uses polynomial regression in the sklearn library to predict the total cases 'n' days after June 29th, 2021. More details below and also comments in the python file. Used NumPy, pandas, sklearn and matplotlib libraries. Has degree=10 in Polynomial_Regression section which gave (using score() function), Accuracy of 99.77%.

Open the CSV/ Excel file for more information regarding the data available about countries, total cases, deaths, and so on.
Dataset - https://ourworldindata.org/coronavirus/country/india

* To run the code, just download the ZIP and unzip it.
* In your choice of Python IDE, import virtualenv and create a virtual environment in the unzipped folder.
* One might need to import the mentioned libraries in the description.
* It is now ready to run!
* 
One can run it as it is, which predicts data of India only.
The CoronaPred.py file can be used to find other country's cases or cases after 29th June 2021.
Use the code in it to change the predictor to predict other country's cases. 
Then pickle the new data. 
Read the comments in CoronaPred.py for more info. 
(To make a different prediction one has to run CoronaPred.py at least once and pickle the regression model.)

Make necessary changes in the app.py file after pickling for proper Matlab plot creation.
