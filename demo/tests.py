from django.test import TestCase
from . import models

# Create your tests here.

class dummyTestCase1(TestCase):
    def test1(self):
        self.assertEqual(1, 1)

class dummyTestCase2(TestCase):
    def test1(self):
        self.assertEqual(1, 1)

class testAddDoctor(TestCase):
    def test1(self):
        d = models.Doctor()
        d.first_name = "John"
        d.last_name = "Becker"
        d.gender = 'M'
        d.speciality = "General Physician"
        d.contact_no = 1234567890
        d.board_reg_no = 'BY13421'
        d.average_time_per_patient = 20
        d.active = 'Y'
        d.save()
        q = models.Doctor.objects.filter(last_name='Becker')[0]
        self.assertEqual(str(d), str(q))