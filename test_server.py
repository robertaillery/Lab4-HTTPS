import unittest
import json
from my_server import app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_factors_endpoint_non_prime(self):
        response = self.app.post('/factors', data=dict(inINT='12'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [2, 2, 3])

    def test_factors_endpoint_prime(self):
        response = self.app.post('/factors', data=dict(inINT='7'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [7])
        
    def test_factors_endpoint_large_number(self):
        response = self.app.post('/factors', data=dict(inINT='360'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [2, 2, 2, 3, 3, 5])

    def test_factors_endpoint_edge_case_one(self):
        response = self.app.post('/factors', data=dict(inINT='1'))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [1])

if __name__ == '__main__':
    unittest.main()