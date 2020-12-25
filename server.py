# import tensorflow as tf
import pandas as pd
from flask import Flask,render_template,request
import numpy as np
import os,time

app = Flask(__name__)

@app.route('/estimate',methods=['POST'])
def estimate_ETA():
    params=request.values.to_dict()
    try:
        print(params,flush=True)
        result=params
    except Exception as e:
        return {'ok': False, 'message': 'Invalid params'},422,{'Access-Control-Allow-Origin': '*'}

    
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