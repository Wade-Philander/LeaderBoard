from tests.base_test import BaseTest, db
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from unittest import TestCase

class TestLogIn(BaseTest):
    def test_that_login_status_200(self):
        with self.app:
            response = self.app.get('/log-in', follow_redirects=True)
            self.assertIn('/log-in', request.url)
            self.assertIn(b'Log in', response.data)
            self.assertEqual(response.status_code, 200)

    def test_if_login_successfully(self):
        with self.app:
            # Sign up
            response = self.app.post('/sign-up',
                           data=dict(email='meh@gmail.com', firstName='NormalName', password1='pass1234', password2='pass1234'),
                           follow_redirects=True)
            self.assertEqual(response.status_code, 200) # it does return the page, just with flash error message
            # assert user is not created
            user = db.session.query(User).filter_by(email='meh').first()
            self.assertFalse(user)
            # assert user is not logged in
            self.assertIsNone(current_user.get_id())

            #Login
            response = self.app.post('/log-in',
                           data=dict(email='meh@gmail.com', firstName='NormalName', password1='pass1234'),
                           follow_redirects=True)
            
            self.assertIn(b'You have logged in' ,response.date)
            self.assertAlmostEqual(response.status_code,200)


            