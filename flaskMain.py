from flask import Flask
import graphCreator as gc
import requests

app = Flask(__name__)

@app.route("/")
def getGraph(payload):
    rawData = requests.get("http://www.localhost:8085/mongoclient/graphrest/getDataForGraph", params=(payload))

    xGraphData = list(rawData.json().values())
    yGraphData = [1,2,3,4,5,6,7,8,9,10]
    gc.makeGraph(xGraphData, yGraphData)
    return "graph created!"

if __name__ == "__main__":
    app.run(debug=False)