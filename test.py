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
        #test whether the api can add a book

        
def test_add_book(self):
        
      response = self.client.post('/api/books/', data=self.book)
      self.assertEqual(response.status_code, 201)
      self.assertIn('coding', str(response.data))
#test whether the api can get  a book by id"""
def test_get_book_by_id(self):
        
        response = self.client.post('/api/books/', data=self.book)
        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.data.decode('utf-8'))
        response_get = self.client.get('/api/books/{}'.format(json_response['book-id']))
        self.assertEqual(response_get, 200)
        self.assertIn('coding', response_get.data)
def test_update_book(self):
       #test whether the api can update book information"""

    response_post = self.client.post('/api/books/', data=self.book)
    self.assertEqual(response_post.status_code, 201)
    book = self.book['publisher'] = 'serah'
    response_put = self.client.put('/api/books/13', data=book)
    self.assertEqual(response_put.status_code, 200)
    response_get = self.client.get('/api/books/13')
    self.assertIn('coding', str(response_get.data))

    def test_get_all_books(self):
        #test whether the api can retrieve all books

        response_post = self.client.post('/api/books/', data=self.book)
        self.assertEqual(response_post.status_code, 201)
        response_get = self.client.get('/api/books/')
        self.assertEqual(response_get.status_code, 200)
        self.assertIn('coding', str(response_get))

    def test_delete_book(self):
        #test whether the api can delete a book"""

        response_post = self.client.post('/api/books/', data=self.book)
        self.assertEqual(response_post.status_code, 201)
        response_delete = self.client.delete('api/books/13')
        self.assertEqual(response_delete.status_code, 200)
        response_get = response_get = self.client.get('/api/books/13')
        self.assertEqual(response_get.status_code, 404)
  
if __name__ == '__main__':
   unittest.main()