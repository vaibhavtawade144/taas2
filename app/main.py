from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/apply-loan", methods=["POST"])
def apply_loan():
    data = request.json
    if data["amount"] < 50000:
        return jsonify({"status": "approved"}), 200
    else:
        return jsonify({"status": "rejected"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
