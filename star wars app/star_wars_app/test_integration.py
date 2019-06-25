import unittest
from star_wars_app import app

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app= app.test_client()

    def test_searchCharacter_getOkResponse(self):
        response = self.app.get('/api/character/luke')
        self.assertEqual(response._status_code,200)

if __name__ == '__main__':
    unittest.main()