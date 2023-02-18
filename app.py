from flask import Flask

app = Flask(__name__)


# decorator to set up route
@app.route("/")
def hello_world():
  return "Hello, Jenks"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
