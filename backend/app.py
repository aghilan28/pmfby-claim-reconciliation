from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

MOCK_DATA = {
    "receipt": {"farmer": "Ravi Kumar", "area": 0.50, "crop": "Rice"},
    "portal":  {"farmer": "Ravi Kumar", "area": 0.45, "crop": "Rice"}
}

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

@app.route('/')
def index():
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(MOCK_DATA)

@app.route('/compare', methods=['POST'])
def compare():
    receipt_area = MOCK_DATA["receipt"]["area"]
    portal_area  = MOCK_DATA["portal"]["area"]
    diff = round(abs(receipt_area - portal_area), 4)
    status = "mismatch" if diff > 0.01 else "match"
    return jsonify({"status": status, "difference": diff})

@app.route('/generate_report', methods=['POST'])
def generate_report():
    receipt_area = MOCK_DATA["receipt"]["area"]
    portal_area  = MOCK_DATA["portal"]["area"]
    diff = round(abs(receipt_area - portal_area), 4)
    farmer = MOCK_DATA["receipt"]["farmer"]
    crop   = MOCK_DATA["receipt"]["crop"]

    if diff > 0.01:
        message = (
            f"PMFBY Claim Reconciliation Report\n"
            f"----------------------------------\n"
            f"Farmer  : {farmer}\n"
            f"Crop    : {crop}\n"
            f"Status  : MISMATCH DETECTED\n"
            f"Receipt Area : {receipt_area} ha\n"
            f"Portal Area  : {portal_area} ha\n"
            f"Difference   : {diff} hectares\n"
            f"Action  : Manual review required before claim approval."
        )
    else:
        message = (
            f"PMFBY Claim Reconciliation Report\n"
            f"----------------------------------\n"
            f"Farmer  : {farmer}\n"
            f"Crop    : {crop}\n"
            f"Status  : ALL FIELDS MATCH\n"
            f"Action  : Claim can be processed automatically."
        )

    return jsonify({"report": message})

if __name__ == '__main__':
    app.run(debug=True)
