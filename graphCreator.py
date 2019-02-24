import matplotlib.pyplot as plt

def makeGraph(x, y):
    graphTitle = "Your Journey"
    xLabel = "Weeks"
    yLabel = "Score"

    plt.grid(True)
    plt.plot(x, y, linewidth=4.0, marker='.', markerfacecolour='green', markersize=13.0)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.suptitle(graphTitle)

    plt.savefig("traineeGraph.svg", bbox_inches='tight')