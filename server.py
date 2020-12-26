# import tensorflow as tf
import pandas as pd
from flask import Flask,render_template,request
import numpy as np
import os,time, datetime,traceback
from geopy.distance import vincenty

def distanceCalc(row):
    '''calculate distance (km) between two lat&long points using the Vincenty formula '''

    return vincenty((row.pickup_lat, row.pickup_lng), (row.dropoff_lat, row.dropoff_lng)).meters/1000.

def distanceCalc(row):
    '''calculate distance (km) between two lat&long points using the Vincenty formula '''

    return vincenty((row.pickup_lat, row.pickup_lng), (row.dropoff_lat, row.dropoff_lng)).meters/1000.



def construct_input_df(obj):
    now=datetime.datetime.now()
    date,hour,min=now.day,now.hour,now.minute
    day_time_range=int(hour*4 + ( np.ceil(min/15) ) )
    input_row=pd.DataFrame([obj])
    input_row['distance']=input_row.apply(lambda x: distanceCalc(x), axis=1)
    input_row['day_time_range'] =  input_row.apply(lambda x: day_time_range, axis=1)
    input_row['date'] =  input_row.apply(lambda x: date, axis=1)

    return input_row

def make_prediction(model,pickup_lat,pickup_lng,dropoff_lat,dropoff_lng):
   
    input_raw={
        "pickup_lat":pickup_lat,
        "pickup_lng":pickup_lng,
        "dropoff_lat":dropoff_lat,
        "dropoff_lng":dropoff_lng

    }
    input_row=construct_input_df(input_raw)
    res=float(model.predict(input_row)[0][0])
    print(res,flush=True)
    return {'eta':res }

app = Flask(__name__)
@app.route('/estimate',methods=['POST'])
def estimate_ETA():
    params=request.values.to_dict()
    try:
        print(params,flush=True)
        pickup_lat=float(params['depLat'])
        pickup_lng=float(params['depLng'])
        dropoff_lat=float(params['arrLat'])
        dropoff_lng=float(params['arrLng'])
        if 'token' in params.keys():
            result={'eta': float(params['token'])}
    except Exception as e:
        return {'ok': False, 'message': 'Invalid params'},422,{'Access-Control-Allow-Origin': '*'}
    try:
      result=make_prediction(model,pickup_lat,pickup_lng,dropoff_lat,dropoff_lng)
      print(result,flush=True)
    except Exception as e: 
      print('Error occured when predicting : ',flush=True)
      traceback.print_exc()
      
      return with_header_response({'ok' : False, 'message': 'An error occured'},500)    

    
    return result,200,{'Access-Control-Allow-Origin': '*'}

 # For Access origin issues
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    response.headers=header
    return response

if __name__ == '__main__':
    app.run(debug=True)    