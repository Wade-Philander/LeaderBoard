from unittest import TestCase
from main import app
from website import db

class BaseTest(TestCase):
    def setUp(self):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.text_client()
        self.app_context = app.app_context

    def tearDown(self):
        # making the database blank
        with app.app_context():
            db.session.remove()
            db.drop_all()