#test for models.py
import unittest
import models

#class to test models
class TestModels(unittest.TestCase):
    def setUp(self):
        self.my_book = models.Books()
        self.my_user = models.Users()
#test that put_book adds book to all_books
    def test_put_book(self):
        result = self.my_book.put("serah chepkirui", "coding", "1st", 1139)
        self.assertIn("serah chepkirui", result['title'])
#tests get_all retrieves all books in the dictionary'''
    def test_get_all_books(self):
        result = self.my_book.get_all()
        self.assertEqual(result, models.all_books)
 #test that edit_book edits
    def test_edit_book(self):
        self.my_book.put("coding in Africa", "serah chepkirui", "13th", 2019)
        result = self.my_book.edit_book("coding in Africa",
                                        "serah chepkirui", "13th", 2019)
        self.assertIn("coding in Africa", result["title"])
#test that get_single_book returns all books
    def test_get_single_book(self):
        self.my_book.put("how to join Andela", "serah chepkirui", "18th", 2)
        result = self.my_book.get_single_book(2)
        self.assertEqual("serah chepkirui", result['author'])
#test that get_single_book returns a book 
    def test_delete_book(self):
        self.my_book.put("coding", "great developers", "6th", 1)
        result = self.my_book.delete(1)
        

        #test that put_user adds
    def test_put_user(self):
        result = self.my_user.put("designers", "great", "serah@gmail.com", "blessings1")
        self.assertIn("great", result)
 #test verify password
    def test_verify_password(self):
        result = self.my_user.verify_password("great", "blessings1")
        self.assertEqual(result, "True")

if __name__ == "__main__":
 unittest.main()