import re
from unittest import TestCase
from main import app
from website import db
from website import Note


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

# INTERGRATION TEST FOR NOTE

class TestModelsCrud(BaseTest):
    def test_note_crud(self):
        with self.app_context:
        #test that notes can be saved and deleted from database

            note = Note(data='New memo')

        #create new note 
            
            results = db.session.query(Note).filter_by(data='new memo').first()
            self.assertIsNone(results)

            #save to database
            db.session.add(note)
            db.session.commit()

            #assert that this item does not exist in database
            results = db.session.query(Note).filter_by(data='new memo').first()
            self.assertIsNotNone(results)


            #delete from database
            db.session.delete(note)
            db.session.commit()

            #delete this item
            results = db.session.query(Note).filter_by(data='new memo').first()
            self.assertIsNone()



