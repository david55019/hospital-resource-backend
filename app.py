from flask import Flask, jsonify 
from datetime import datetime 
app = Flask(__name__) 
hospital_resources = [ 
    {"id": 1, "hospital_name": "City Hospital", "resource_type": "ICU Beds", "available": 5, "last_updated": str(datetime.now())}, 
    {"id": 2, "hospital_name": "County Hospital", "resource_type": "General Beds", "available": 40, "last_updated": str(datetime.now())} 
] 
@app.route("/") 
def home(): 
    return jsonify({"message": "Hospital Resource API running"}) 
@app.route("/resources", methods=["GET"]) 
def get_resources(): 
    return jsonify(hospital_resources) 
if __name__ == "__main__": 
    app.run(debug=True, port=5000) 
