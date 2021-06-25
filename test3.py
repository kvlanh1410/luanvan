# librarie
from flask import Flask, render_template, request,redirect
from flask_ngrok import run_with_ngrok
import nltk
from waitress import serve
app = Flask(__name__)
# run_with_ngrok(app)
