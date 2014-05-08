from flask import Flask
from flask.ext.restless import APIManager
from itpdir.authn import login_manager, auth_func
from itpdir.config import config
from itpdir.database import Base, db_session, engine
from itpdir.models import Person

app = Flask(__name__)
app.secret_key = config.get('secrets', 'SECRET')

# Flask-Login and authn code
login_manager.init_app(app)

# Flask-Restless API endpoints
# note: GET preprocessors pulled in via itpdir.authn.auth_func
manager = APIManager(app, session=db_session, preprocessors=dict(GET_SINGLE=[auth_func], GET_MANY=[auth_func]))
person_blueprint = manager.create_api(Person, methods=['GET'], collection_name='person', url_prefix='/v1')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
