from datetime import date
from unittest import TestCase
import sys
sys.path.append("website\models")
from website.models import Note, Work, User, Team

class TestModel(TestCase): 
    def test_note(self):
        i = Note(data="Test", date=2021/5/19,  user_id=2)

        self.assertEqual(i.data,'Test')
        self.assertEqual(i.date, 2021/5/19, "is todays date")
        self.assertEqual(i.user_id, 2)

    def test_work(self):
        a = Work(title="Title", description="This is a Test", date=2021/5/19, status=100, points=500000)
        
        self.assertEqual(a.title,'Title')
        self.assertEqual(a.description,'This is a Test')
        
        self.assertEqual(a.date, 2021/5/19, "Is the date")
        self.assertEqual(a.status, 100, "pass")
        self.assertEqual(a.points,500000)

    def test_user(self):
        user = User(email="gmail.com", password="qwerty", first_name="Wade", team_leader=True, points=10)

        
        self.assertEqual(user.email, "gmail.com")
        self.assertEqual(user.password, "qwerty")
        self.assertEqual(user.first_name, "Wade")
        self.assertIsNotNone(user.notes)
        self.assertEqual(user.team_leader, True)
        self.assertEqual(user.points,10)

    def test_team(self):
        team = Team(id=5, name="Haikyuu!!:To the Top")

        self.assertEqual(team.id, 5)
        self.assertEqual(team.name, "Haikyuu!!:To the Top")
        




