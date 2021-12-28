# FlaskBlog

Following flask tutorial from Corey Schafer

## Create Database

- Install the `requirements.txt`
  
  ```txt
  pip install -r requirements.txt
  ```

- Edit `flaskblog/__init__.py`
  
  ```python
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:pass@localhost/db_name'
  ```

  replace `username`, `pass`, `localhost` and `db_name` with appropriate
  database configuration in your computer or server

- Log in into your mysql console and create `db_name` database

- Open python REPL under this directory and run the following command:

  ```txt
  >>> from flaskblog import app, db
  >>> app.app_context().push()
  >>> db.create_all() 
  ```
