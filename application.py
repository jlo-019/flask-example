from flask import Flask
from flask import Flask, request, jsonify, render_template
import torch
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import boto3
import os
from io import BytesIO
from torch import nn

application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('query.html')