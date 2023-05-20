import json
import argparse
import csv
from jinja2 import Template
from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

argsToParse = argparse.ArgumentParser(description="Kuros Trading Visualizer - @devkuro - GH: im-kuro")
argsToParse.add_argument("--filepath", "-f", help="the file/path to the csv file", default=False, type=str)
argParsedObj = argsToParse.parse_args()

order_types = {
    "0": "Buy",
    "1": "Sell",
    "2": "Buy Limit",
    "3": "Sell Limit",
    "4": "Buy Stop",
    "5": "Sell Stop"
}

color_map = {
    "-": "red",  # loss
    "$": "green",  # profit
    "N": "yellow",  # no trade
}


def parseCSVDataToJSON(pathToCSV: str) -> dict:
    jsonData = defaultdict(dict)

    with open(pathToCSV, "r") as openCSVFile:
        csvreader = csv.reader(openCSVFile)
        fields = next(csvreader)  # extracting field names through first row

        for row in csvreader:  # extracting each data row one by one
            trade = {
                "orderType": order_types.get(row[1], ""),
                "symbol": row[2],
                "volume": row[3],
                "sl": row[4],
                "tp": row[5],
                "openedAt": row[6],
                "closedAt": row[7],
                "swaps": row[8],
                "commission": row[9],
                "profitloss": row[10],
                "comment": row[11],
                "color": next((color for color, symbol in color_map.items() if str(row[10]).startswith(symbol)), "orange")
            }
            jsonData["trades"][row[0]] = trade

    return jsonData


@app.route('/', methods=['GET', 'POST'])
def trade_history():
    jsonData = parseCSVDataToJSON(argParsedObj.filepath)
    return render_template('main.html', trades=jsonData)


if __name__ == "__main__":
    print("Kuros Trading Visualizer - @devkuro - GH: im-kuro\n\n")
    if argParsedObj.filepath == False:
        print("Error: No file path was given")
        exit(0)

    app.run()
