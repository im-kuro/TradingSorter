import json
import argparse
import csv
from jinja2 import Template
from flask import Flask, render_template, request

app = Flask(__name__)

argsToParse = argparse.ArgumentParser(description="Kuros Trading Visualizer - @devkuro - GH: im-kuro")

argsToParse.add_argument("--filepath", "-f", help="the file/path to the csv file", default=False, type=str)

argParsedObj = argsToParse.parse_args()


def pharseCSVDataToJSON(pathToCSV: str) -> dict:

    jsonData = {
        "trades": {}
    }

    with open(pathToCSV, "r") as openCSVFile:
        csvreader = csv.reader(openCSVFile)
        fields = next(csvreader)  # extracting field names through first row

        for row in csvreader:  # extracting each data row one by one
            trade = {
                "orderType": row[1],
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
                "color": ""
            }
            # check if its no profit/profit/loss
            if str(row[10][0]) == "-": # loss
                trade["color"] = "red"
            elif str(row[10][0]) == "$": # profit
                trade["color"] = "green"
            elif str(row[10][0]) == "N": # no trade
                trade["color"] = "yellow"
            else:
                trade["color"] = "orange" # unknown
             # check for order Type
            if trade["orderType"] == "0":
                trade["orderType"] = "Buy"
            if trade["orderType"] == "1":
                trade["orderType"] = "Sell"
            if trade["orderType"] == "2":
                trade["orderType"] = "Buy Limit"    
            if trade["orderType"] == "3":  
                trade["orderType"] = "Sell Limit"
            if trade["orderType"] == "4":    
                trade["orderType"] = "Buy Stop" 
            if trade["orderType"] == "5":   
                trade["orderType"] = "Sell Stop"
		
            jsonData["trades"][f"{row[0]}"] = trade

        return jsonData



@app.route('/', methods=['GET', 'POST'])
def trade_history():
    
    jsonData = pharseCSVDataToJSON(argParsedObj.filepath)
	
    return render_template('main.html', trades=jsonData)



if __name__ == "__main__":
    print("Kuros Trading Visualizer - @devkuro - GH: im-kuro\n\n")
    if argParsedObj.filepath == False:
        print("Error: No file path was given")
        exit(0)


    app.run()










