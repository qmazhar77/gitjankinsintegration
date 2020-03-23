import unittest

def setUpModule():
    print("Setup Module")

def tearDownModule():
    print("Tear Down Module")

class Apptesting(unittest.TestCase):

    @classmethod
    def setUp(self):
        print ("This is Login Test")

    @classmethod
    def tearDown(self):
        print("This is Logout test")

    @classmethod
    def setUpClass(cls):
        print("This is lunch application")

    @classmethod
    def tearDownClass(cls):
        print("This is close application")

    def test_search(self):
        print("This is search test")

    def test_advanceserach(self):
        print("This is advance serach")

    def test_postpaid(self):
        print("This is postpaid")

    def test_prepaid(self):
        print("This is prepaid")

