import unittest
import json
from flask import Flask
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_sort_integers_valid_input(self):
        data = {'arr': [0, 1, 2, 3, 4, 5, 6, 7, 8]}
        response = self.app.post('/sort', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['sorted_arr'], [0, 1, 2, 4, 8, 3, 5, 6, 7])

    def test_sort_integers_empty_input(self):
        data = {'arr': []}
        response = self.app.post('/sort', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['sorted_arr'], [])

    def test_sort_integers_invalid_input_not_a_list(self):
        data = {'arr': 'not a list'}
        response = self.app.post('/sort', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Input must be a list')

    def test_sort_integers_invalid_input_non_integer(self):
        data = {'arr': [1, 'a', 2]}
        response = self.app.post('/sort', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'All elements must be integers')

    def test_sort_integers_input_size_exceeded(self):
        data = {'arr': list(range(1001))}
        response = self.app.post('/sort', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data)
        self.assertEqual(result['error'], 'Input array size exceeds the limit (1000)')

if __name__ == '__main__':
    unittest.main()
