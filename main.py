from flask import Flask, jsonify, abort, request
app = Flask(__name__)
books = [
{
"book_id":13,
"Name":"coding",
"Author":"serah",
"Publisher":"serah",
"Copies":10,
"Pages":500,
	
},
{
"book_id":114,
"Name":"coding in kenya",
"Author":"chepkirui",
"Publisher":"serah",
"Copies":10,
"Pages":500,
}
    ]

#This is the API for adding a book
@app.route('api/books', methods=['POST'])
def add_book():
	book = {
	'id': request.json['id'],
	'Name': request.json['Name'],
	'Author': request.json['Author'],
	'Publisher': request.json['publisher'],
	'Copies': request.json['Copies']
 	}
	books.append(book)
	return jsonify({'book': book}), 201
#viewing all books
@app.route('api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

    
#This is API for updating a book information
@app.route('api/books/<int:id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    book[0]['id'] = request.json.get('id', book[0]['id'])
    book[0]['Name'] = request.json.get('Name', book[0]['Name'])
    book[0]['Author'] = request.json.get('Author', book[0]['Author'])
    book[0]['Publisher'] = request.json.get('Publisher', book[0]['Publisher'])
    book[0]['Copies'] = request.json.get('Copies', book[0]['Copy'])
    return jsonify({'book': book[0]})
    @app.route('/api/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    
#This code updates, deletes or retrieves a specific book with a given an id"""
    @app.route('api/books/<int:id>', methods=['DELETE'])
    def get_books(id):
      

        if not book:
            abort(404)
   
        if request.method == 'DELETE':
            book.delete()
        return {'message': 'success'}, 200


if __name__ == "__main__":
 app.run(debug=True)