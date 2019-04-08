from flask import Flask, jsonify, request
from keras.models import load_model
from keras import backend as K
import pandas as pd
import json
import numpy as np


app = Flask(__name__)





@app.route('/data/api/v1.0/test_data',methods=['POST','GET',])
def test_data():

    if request.method == 'POST':
        data = request.get_json(force=True)

        # get data from json post request
        X_new_json = data['test_data']

        # load saved model
        trained_model = load_model('trained_model.h5')

        # Convert data to numpy array
        X_new = np.array([X_new_json])
        print(X_new)

        # from trained model predict Y values
        y_new = trained_model.predict(X_new)

        #after predicting my data i inserted this part of code then i had again loaded the model
        K.clear_session()

        # read and get length of complete rows
        dfObj = pd.read_csv("Predictions.csv")
        len_index = len(dfObj['ID'])
        # print(len_index+1)

        dict = {}

        # append data to dictnary
        dict.update({"ID": [len_index + 1], "Data": [X_new[0]], "Predicted": [y_new[0]]})

        # convert it to dataframe to can put to csv
        df = pd.DataFrame(dict)

        # open csv file flag "a" to append data and header which is columns would be only one time  bcs of header=f.tell() == 0
        with open("Predictions.csv", 'a') as f:
            df.to_csv(f, mode='a', index=False, header=f.tell() == 0)


        #print values inputed and pridected
        print("X=%s, Predicted=%s" % (X_new[0], y_new[0]))

        x_new_json = json.loads(df["Data"].to_json(orient='records'))
        y_new_json = json.loads(df["Predicted"].to_json(orient='records'))
        print(x_new_json)


        return jsonify({X_new_json:y_new_json})



    elif request.method == 'GET':



        return jsonify({"GET Method":"Data"})



if __name__ == '__main__':
    app.run(debug=True ,threaded=True)