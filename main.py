import flask
from flask import request, jsonify
import csv
import json
app = flask.Flask(__name__)

def make_json(csvFilePath, jsonFilePath, format):
    data = {}
    with open(f'./data/{csvFilePath}', encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            key = rows[format]
            data[key] = rows
 
    with open(f'./data/{jsonFilePath}', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

make_json(r'data_latest.csv', r'Cryptocurrency.json', 'Cryptocurrency')

with open('./data/Cryptocurrency.json') as json_file:
    Cryptocurrency = json.load(json_file)
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "Hello World!"

@app.route('/api/all', methods = ['GET'])
def all():
    return jsonify(Cryptocurrency)

@app.route('/api/crypto?req=<Cryptocurrency>', methods = ['GET'])
def country():
    if 'req' in request.args:
        req = str(request.args['req'])
        req = req.upper()
        for i in Cryptocurrency:
            if i == req:
                results_code = (Cryptocurrency[i])
        return jsonify(results_code)
       
    else:
        return "Error: No valid crypto code provided."

    # if len(req) == 3:
    #     for i in Cryptocurrency:
    #         if i == req:
    #             results_code = (Cryptocurrency[i])
    #     return jsonify(results_code)
    # else:
    #     return "Error: No valid ISO2 or ISO3 country code provided."

    # For Debugging    
# app.run()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=80)