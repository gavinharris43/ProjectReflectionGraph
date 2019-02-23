import requests
import matplotlib.pyplot as plt

rawData = requests.get("http://www.localhost:8085/graphrest/getDataForGraph")

graphTitle = "Your Journey"
xLabel = "Weeks"
yLabel = "Score"

xGraphData = list(rawData.json().values())
yGraphData = [1,2,3,4,5,6,7,8,9,10]

plt.grid(True)
plt.plot(xGraphData, yGraphData, linewidth=4.0, marker='.', markerfacecolour='green', markersize=13.0)
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.suptitle(graphTitle)

plt.savefig("traineeGraph.svg", bbox_inches='tight')