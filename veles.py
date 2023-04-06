from data import ROD, db_session
from flask import Flask

app = Flask(__name__)


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(ROD.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()