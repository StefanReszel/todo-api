import os
from todo_api import create_app, db


if __name__ == '__main__':
    app = create_app()

    if not os.path.exists('db.sqlite3'):
        db.create_all(app=app)

    app.run()