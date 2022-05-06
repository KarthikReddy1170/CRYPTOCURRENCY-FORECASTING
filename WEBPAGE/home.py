# from application import app
from flask import *
import pandas as pd
import json
import plotly
import plotly.express as px
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route("/BTC")
def index_BTC():
    # Graph One
    df = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT NEW\\BITCOINPREDICTION\\BTC-USD.csv")
    fig1 = px.bar(df, x="Date", y="Close",title="BITCOIN INFO")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # Graph two
    df2 = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT NEW\\BITCOINPREDICTION\\BTCPREDC.csv")
    fig2 =  px.line(df2, x="DATE", y="PREDICTION",title="BITCOIN PREDICTION VALUE")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('BTCindex.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON)
@app.route("/datasetBTC")
def dataset_display_BTC():
    return render_template("BTCdataset.html")
@app.route("/ETH")
def index_ETH():
    # Graph One
    df = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT\\AI FOR DS PROJECT\\ETHERUM\\ETH-USD.csv")
    fig1 = px.bar(df, x="Date", y="Close", title="ETHEREUMS INFO")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # Graph two
    df2 = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT\\ETHERUMFORECASTIN.csv")
    fig2 = px.line(df2, x="DATE", y="PREDICTION", title="ETHEREUMS PREDICTION VALUE")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('ETHindex.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON)
@app.route("/datasetETH")
def dataset_display_ETH():
    return render_template("ETHdataset.html")
@app.route("/home")
def home_page():
    return render_template("home.html")
@app.route("/SAND")
def index_SAND():
    # Graph One
    df = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT NEW\\SANDBOX\\SAND-USD.csv")
    fig1 = px.bar(df, x="Date", y="Close",title="SANDBOX'S INFO")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # Graph two
    df2 = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT NEW\\SANDBOX\\SANDPREDC-1.csv")
    fig2 =  px.line(df2, x="DATE", y="PREDICTION",title="SANDBOX'S PREDICTION VALUE")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('SANDindex.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON)
@app.route("/datasetSAND")
def dataset_display_SAND():
    return render_template("SANDdataset.html")
if __name__=='__main__':
    app.run(debug=True)