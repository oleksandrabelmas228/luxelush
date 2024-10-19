from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/luxelush"
app.config['SECRET_KEY'] = 'bebra'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models


if __name__ == '__main__':
    app.run(debug=True)