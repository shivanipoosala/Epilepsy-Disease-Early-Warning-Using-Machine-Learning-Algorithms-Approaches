from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
df=pd.read_csv("Epilepsy_Dataset.csv")
app = Flask(__name__)

#Deserialize
model = pickle.load(open('model.pkl','rb'))
df = df.drop(df.columns[[0, 1]],axis = 1)
df = df.rename(columns={"Brain_tumor(stage)": "Brain_tumor"})


@app.route('/')
def index():
    return render_template("index.html") #due to this function we are able to send our webpage to client(browser) - GET

@app.route('/predict',methods=['POST','GET'])  #gets inputs data from client(browser) to Flask Server - to give to ml model
def predict():
    if request.method == 'POST':
        features = [int(x) for x in request.form.values()]
        print(features)
        final = [np.array(features)]
    #our model was trained on Normalized(scaled) data
        X = df.iloc[:, 0:18].values
        sst=StandardScaler().fit(X)
        output = model.predict(sst.transform(final))
        print(output)

        if output[0]==0:
            return render_template("predict.html", prediction =0)
        else:
            return render_template("predict.html", prediction = 1)


    #return render_template("predict.html",prediction=res)
if __name__ == '__main__':
    app.run(debug=True)