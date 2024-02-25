import unittest
from Project_API import create_app,app #create_app wrapper for testing and app export 

class API_Tests(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
    
    def test_api_server_status(self):
        response = self.app.get('/') # or homepage if no / exists
        self.assertEqual(response.status_code,200)

    def test_api_server_nbapage(self):
        response = self.app.get('/nba')
        self.assertEqual(response.status_code,200)
    
    def tearDown(self):
        self.app.get('/shutdown',follow_redirects=True)

class NBA_Page_Tests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_nba_data_response(self):
        #not necessarily valid data but that response data is not empty
        response = self.app.get('/nba_data')
        self.assertGreater(len(response.get_json()),0)
    
    def tearDown(self):
        self.app.get('/shutdown',follow_redirects=True)
        
if __name__ == '__main__':
    unittest.main()