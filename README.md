# Book Collection Manager

A CLI application to manage your personal book collection.

## Features

- Add new books with title, author, and genre
- View all books in your collection
- Update book details
- Delete books from collection
- Search books by title or author

## User Stories

1. As a user, I can add a new book with details such as title, author, and genre.
2. As a user, I can view all books in my collection.
3. As a user, I can update a book's details (title, author, or genre).
4. As a user, I can delete a book from my collection.
5. As a user, I can search for books by title or author.

## Installation

```bash
# Clone the repository
git clone https://github.com/sydney-lab/final-project.git
cd final-project

# Install dependencies
pip install --break-system-packages -r requirements.txt

# Run the application
python3 cli.py --help
```

## Usage

```bash
# Add a new book
python3 cli.py add

# View all books
python3 cli.py list

# Search for books
python3 cli.py search "harry potter"

# Update a book (use ID from list command)
python3 cli.py update 1

# Delete a book (use ID from list command)
python3 cli.py delete 1
```