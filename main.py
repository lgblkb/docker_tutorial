from pprint import pformat

from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    vals = np.random.rand(10, 2)
    return dict(vals=str(vals), qwe=123, message='Salem')


@app.route("/bye")
def bye_world():
    vals = np.random.rand(10, 2)
    return dict(vals=str(vals), qwe=123, message='Bye')

