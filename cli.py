import click
from models import Book, Session

@click.group()
def cli():
    """Book Collection Manager - Manage your personal book collection"""
    pass

@cli.command()
@click.option('--title', prompt='Book title', help='Title of the book')
@click.option('--author', prompt='Author name', help='Author of the book')
@click.option('--genre', prompt='Genre', help='Genre of the book')
def add(title, author, genre):
    """Add a new book to your collection"""
    session = Session()
    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    click.echo(f"Added '{title}' by {author} to your collection!")
    session.close()

@cli.command()
def list():
    """View all books in your collection"""
    session = Session()
    books = session.query(Book).all()
    if not books:
        click.echo("No books in your collection yet.")
    else:
        click.echo("\nYour Book Collection:")
        for book in books:
            click.echo(f"ID: {book.id} | {book.title} by {book.author} ({book.genre})")
    session.close()

@cli.command()
@click.argument('book_id', type=int)
def update(book_id):
    """Update a book's details"""
    session = Session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        click.echo("Book not found!")
        return
    
    book.title = click.prompt('New title', default=book.title)
    book.author = click.prompt('New author', default=book.author)
    book.genre = click.prompt('New genre', default=book.genre)
    
    session.commit()
    click.echo(f"Updated book ID {book_id}!")
    session.close()

@cli.command()
@click.argument('book_id', type=int)
def delete(book_id):
    """Delete a book from your collection"""
    session = Session()
    book = session.query(Book).filter(Book.id == book_id).first()
    if not book:
        click.echo("Book not found!")
        return
    
    if click.confirm(f"Delete '{book.title}' by {book.author}?"):
        session.delete(book)
        session.commit()
        click.echo("Book deleted!")
    session.close()

@cli.command()
@click.argument('query')
def search(query):
    """Search for books by title or author"""
    session = Session()
    books = session.query(Book).filter(
        (Book.title.contains(query)) | (Book.author.contains(query))
    ).all()
    
    if not books:
        click.echo(f"No books found matching '{query}'")
    else:
        click.echo(f"\nBooks matching '{query}':")
        for book in books:
            click.echo(f"ID: {book.id} | {book.title} by {book.author} ({book.genre})")
    session.close()

if __name__ == '__main__':
    cli()