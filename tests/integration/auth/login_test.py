from tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User

class TestLogin(BaseTest):
    def test_login_with_existing_user(self):
        with self.app:
            #Create a post req with valid data
            response = self.app.post('/sign-up',data=dict(email='email@gmail.com', firstName='Namey', password1='pass1234', password2='pass1234')
            ,follow_redirects=True)
            #assert that new user is created
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)
            response = self.app.post('/log-in',data=dict(email='email@gmail.com', password='pass1234'))
            self.assertTrue(current_user.is_active)

    def test_logi_with_incorrect_password(self):
        with self.app:
            response = self.app.get('/sign',follow_redirects=True)
            self.assertIn
            