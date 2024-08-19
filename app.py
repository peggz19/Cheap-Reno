# Import the dependencies.

from flask import Flask, jsonify, render_template, request


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#1. Main Page + Charts
    #Below I am taking a random index.html file to test
@app.route("/")
def main():
    return (render_template('website.html', is_landing=True))