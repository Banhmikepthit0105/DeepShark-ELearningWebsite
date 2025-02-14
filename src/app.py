from flask import Flask, render_template
from api.routes.routes import api_bp
from api.settings import db, bcrypt, jwt
from flask_migrate import Migrate
import os

from api.routes.auth import app as auth_bp
from flask import Flask


from dotenv import load_dotenv
import psycopg2

load_dotenv()


app = Flask(__name__)

# Config from .env
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(api_bp, url_prefix="/api/ai_models/")
app.register_blueprint(auth_bp, url_prefix="/api/auth/")


@app.route("/")
def home():
    return render_template("index.html", name="home.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("index.html", name="login.html")


@app.route("/sign-up", methods=["GET"])
def signUp():
    return render_template("index.html", name="sign-up.html")


@app.route("/question", methods=["GET"])
def question():
    return render_template("index.html", name="question.html")


def get_db_course():
    conn = psycopg2.connect(host="ml-web.postgres.database.azure.com", database="courses", user="ml_admin", password="ml#web_db#2224")
    return conn


@app.route("/tutorial", methods=["GET"])
def tutorial():
    conn = get_db_course()
    cur = conn.cursor()
    cur.execute("SELECT name, link, image FROM courses")
    courses = cur.fetchall()
    cur.close()
    return render_template("index.html", name="tutorial.html", courses=courses)


@app.route("/chat", methods=["GET"])
def chat():
    return render_template("index.html", name="chat.html")


if __name__ == "__main__":
    app.run(debug=True)
