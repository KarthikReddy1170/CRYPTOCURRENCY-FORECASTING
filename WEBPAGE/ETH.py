# from application import app
from flask import *
import pandas as pd
import json
import plotly
import plotly.express as px
app=Flask(__name__)
@app.route("/ETH")
def index():
    # Graph One
    df = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT\\AI FOR DS PROJECT\\ETHERUM\\ETH-USD.csv")
    fig1 = px.bar(df, x="Date", y="Close", title="ETHEREUMS INFO")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # Graph two
    df2 = pd.read_csv("C:\\2 ND YEAR\\PROJECTS\\AI FOR DS PROJECT\\ETHERUMFORECASTIN.csv")
    fig2 = px.line(df2, x="DATE", y="PREDICTION", title="ETHEREUMS PREDICTION VALUE")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    # # Graph three
    # fig3 =  px.bar(df, x="category_id", y="views",title="views from each category")
    # graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('ETHindex.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON)
@app.route("/datasetETH")
def dataset_display():
    return render_template("ETHdataset.html")
# @app.route("/ml")
# def ml_display():
#     return render_template("ml.html")
@app.route("/home")
def home_page():
    return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)