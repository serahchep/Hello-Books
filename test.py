#test_main.py
import unittest
import json
from API import app

class TestApiEndpoints(unittest.TestCase):
    def setUp(self):
        with app.APP.app_context():
            self.client = app.APP.test_client
    #test that API can add a book 
    def test_api_can_add_book(self):
        
        response = self.client().post('/api/v1/books', data=json.dumps(
            {"book_id":20, "title": "coding",
             "author":"serah"}),
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)
#test that api can get all books (GET request)
    def test_api_can_get_all_books(self):
        response = self.client().get('/api/v1/books')
        self.assertEqual(response.status_code, 200)
 #test that api can retrieve book by id (GET request)
    def test_api_can_get_book_by_id(self):
        response = self.client().get('/api/v1/books/2')
        self.assertEqual(response.status_code, 200)
        self.assertIn("queens are beatifull", str(response.data))
    #test that api can modify book
    def test_book_can_be_edited(self):
        res = self.client().put('/api/v1/books/2',
                                data=json.dumps({"title":"talents", 
                                                 "author":"serah",
                                                 "edition": "8th"}), 
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        results = self.client().get('/api/v1/books/2')
        self.assertIn("John Greene", str(results.data))
#test that api can delete book (POST request)
    def test_delete_book(self):
        res = self.client().post('/api/v1/books', content_type='application/json',
                                 data=json.dumps({"book_id":16,
                                                  "title": "gifts",
                                                  "author": "serah"}))
        self.assertEqual(res.status_code, 200)
        res = self.client().delete('/api/v1/books/16')
        #test to check whether deleted item exists
        self.assertEqual(res.status_code, 200)
        result = self.client().get('/api/v1/books/16')
        self.assertIn("Book not found", result.data)
 #method to test register 
        result = self.client().post('/api/v1/auth/register', content_type='application/json',
                                    data=json.dumps({"username":"serah", "name":"chepkiruiserah",
                                                     "email":"serahkaku254@gmail.com", "password":"blessings1",
                                                     "confirm_password":"blessings1"}))
        self.assertEqual(result.status_code, 200)
        #method to test register login
        result2 = self.client().post('/api/v1/auth/login', content_type='application/json',
                                     data=json.dumps({"username":"serah", "password":"blessings1"}))
        a_token = result2.data
        self.assertEqual(result2.status_code, 200)

        result3 = self.client().post('/api/v1/users/books/2',
                                     headers=dict(Authorization="Bearer "+ a_token))
        self.assertEqual(result3.status_code, 200)

        result4 = self.client().post('/api/v1/auth/logout',
                                     headers=dict(Authorization="Bearer " + a_token))
        self.assertIn('Successfully logged out', result4.data)

        result5 = self.client().post('/api/v1/auth/reset-password', content_type='application/json',
                                     data=json.dumps({"username":"hawa"}))
        self.assertEqual(result5.status_code, 200)

if __name__ == "__main__":
 unittest.main()