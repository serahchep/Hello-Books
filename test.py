import unittest
import json
from app import app
def setUp(self):
        self.app = app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context.push()
        self.book = {
           "book_id":13,
           "Name":"coding",
           "Author":"serah",
           "Publisher":"serah",
           "Copies":10,
           "Pages":500,
	
        }
        #test whether the api can add a book"""

        
def test_add_book(self):
        
      response = self.client.post('/api/books/', data=self.book)
      self.assertEqual(response.status_code, 201)
      self.assertIn('coding', str(response.data))
#test whether the api can retrieve a book by id"""
def test_get_book_by_id(self):
        
        response = self.client.post('/api/books/', data=self.book)
        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.data.decode('utf-8'))
        response_get = self.client.get('/api/books/{}'.format(json_response['book-id']))
        self.assertEqual(response_get, 200)
        self.assertIn('coding', response_get.data)

  
if __name__ == '__main__':
   unittest.main()