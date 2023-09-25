from sqlalchemy import create_engine,text

# create_engine(URL / path to database, to be able to see what is going on the database side)
engine = create_engine("sqlite:///sample.db",echo=True)

# create connection object
# use 'as connection' to hide whats been brought forth
with engine.connect() as connection:
    # does a query
    result = connection.execute(text('select "Hello"'))

    print(result.all())