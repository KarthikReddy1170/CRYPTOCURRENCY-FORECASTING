# from application import app
from flask import *
import pandas as pd
import json
import plotly
import plotly.express as px
app=Flask(__name__)
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
    # # Graph three
    # fig3 =  px.bar(df, x="category_id", y="views",title="views from each category")
    # graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('SANDindex.html', graph1JSON=graph1JSON, graph2JSON=graph2JSON)
@app.route("/datasetSAND")
def dataset_display_SAND():
    return render_template("SANDdataset.html")
# @app.route("/ml")
# def ml_display():
#     return render_template("ml.html")
@app.route("/home")
def home_page():
    return render_template("SANDhome.html")
if __name__=='__main__':
    app.run(debug=True)