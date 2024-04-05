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

'''
# Initialize Boto3 S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AKIAQFX7EOOG5PE3GORJ'),
    aws_secret_access_key=os.getenv('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'),
    region_name='eu-west-2'
)

bucket_name = 'oritsejolomi-fyp'

# Load the precomputed code embeddings and raw code snippets from S3 bucket
code_embeddings = None
combined_raw_code = None
with BytesIO() as data:
    s3_client.download_fileobj(bucket_name, 'code_embeddings.npy', data)
    data.seek(0)
    code_embeddings = np.load(data, allow_pickle=True)

    s3_client.download_fileobj(bucket_name, 'combined_raw_code.pkl', data)
    data.seek(0)
    combined_raw_code = pickle.load(data)
    # using s3_client.download_fileobj can be more memory-efficient since it allows to read contents 
    # of S3 objects directly into memory without storing them on disk,

# Load the pre-trained model
model = SentenceTransformer('model_directory')

#Define cosine_similarity to be accessible everywhere 
cosine_similarity = nn.CosineSimilarity(dim=1)

'''
@application.route('/')
def hello_world():
    return render_template('query.html')