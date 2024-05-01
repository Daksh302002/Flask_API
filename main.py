from flask import Flask, jsonify, request

app = Flask(__name__)


books = [

    {'id': 1, 'title': 'book 1', 'author': 'author 1'},
    {'id': 2, 'title': 'book 2', 'author': 'author 2'},
    {'id': 3, 'title': 'book 3', 'author': 'author 3'}

]

# Get a book


@app.route("/books", methods=['GET'])
def get_books():
    return books

# Get a book by specific Id


@app.route("/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return "<h1>Error Book not found!!</h1>"


# Create A book

@app.route("/books", methods=['POST'])
def create_book():
    new_books = {"id": len(
        books)+1, "title": request.json["title"], "author": request.json["author"]}
    books.append(new_books)
    return new_books


# update a book

@app.route("/books/<int:book_id>", methods=["PUT"])
def update(book_id):
    for book in books:
        if book["id"] == book_id:
            book["title"] = request.json['title']
            book['author'] = request. json['author']
            return book
    return "Error Book not found!"


# Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"data": "book deleted successfully"}

    return "Error Book not found!"


if __name__ == "__main__":
    app.run(debug=True)
