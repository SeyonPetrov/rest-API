import flask
from flask import jsonify
from data import db_session
from data.jobs import Jobs


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_news():
    item = db_session.create_session().query(Jobs).all()
    return jsonify(
        {
            'news':
                [x.to_dict() for x in item]
        }
    )
