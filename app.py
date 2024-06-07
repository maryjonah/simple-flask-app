from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
  return jsonify({'hello': 'from template api auto-deployed with GitHub actions and being tested!'}), 200


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  