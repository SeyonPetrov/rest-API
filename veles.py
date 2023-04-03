from data import db_session, jobs


def main():
    db_session.global_init("db/blogs.db")
    app.register_blueprint(jobs.blueprint)
    app.run()