from flask import Flask
from bookstore import app, db

if __name__ == "__main__":
    db.create_all()
    app.run(debug=False)
