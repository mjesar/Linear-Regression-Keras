from flask import Flask, jsonify, request
from keras.models import load_model
from keras import backend as K

import numpy as np


app = Flask(__name__)





@app.route('/data/api/v1.0/test_data',methods=['POST','GET',])
def test_data():

    if request.method == 'POST':
        data = request.get_json(force=True)

        # get data from json post request
        X_new = data['test_data']

        # load saved model
        trained_model = load_model('trained_model.h5')

        # Convert data to numoy array
        X_new = np.array([X_new])
        print(X_new)

        # from trained model predict Y values
        y_new = trained_model.predict(X_new)

        K.clear_session()

        #print values inputed and pridected
        print("X=%s, Predicted=%s" % (X_new[0], y_new[0]))
        return jsonify({"POST Method ":""})

    elif request.method == 'GET':



        return jsonify({"GET Method":"Data"})



if __name__ == '__main__':
    app.run(debug=True ,threaded=True)