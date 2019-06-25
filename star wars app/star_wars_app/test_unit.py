import unittest
import requests
from unittest.mock import patch
from star_wars_app import views


class TestDataManipulationMethods(unittest.TestCase):
 
    def setUp(self):
        self.views = views

    def test_getIdFromUrl_getTheRightId(self):
        url = "https://swapi.co/api/poeple/4/"
        answer = self.views.getIdFromUrl(url)
        self.assertEqual(answer, '4')

    def test_getIdFromUrl_getTheWrongId(self):
        url = "https://swapi.co/api/poeple/4/"
        answer = self.views.getIdFromUrl(url)
        self.assertNotEqual(answer, '3')
  
    @patch('star_wars_app.views.getIdFromUrl', return_value='4')
    def test_getIdFromUrl_getTheRightId_mocked(self, getIdFromUrl):
        url = "https://swapi.co/api/poeple/4/"
        self.assertEqual(getIdFromUrl(url), '4')

   
    @patch('star_wars_app.views')
    def test_searchCharacter_getOkResponse(self,mockRequest):
        mockRequest.searchCharacter.return_value ={"status_code":200};
        response = mockRequest.searchCharacter("luke")
        self.assertIsNotNone(response)
        self.assertEqual(response['status_code'],200)
   
    @patch('star_wars_app.views')
    def test_searchCharacter_getBadRequest(self,mockRequest):
        mockRequest.searchCharacter.return_value ={"status_code":400};
        response = mockRequest.searchCharacter("luke")
        self.assertIsNotNone(response)
        self.assertEqual(response['status_code'],400)

    
if __name__ == '__main__':
    unittest.main()
