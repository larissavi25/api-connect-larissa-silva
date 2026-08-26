from flask import Flask

from routes.connect_routes import connect_routes


app = Flask(__name__)

app.register_blueprint(connect_routes)


@app.route("/")
def home():
    return {
        "message": "API Connect funcionando!"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
