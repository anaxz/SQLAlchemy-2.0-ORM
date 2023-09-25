from models import Base, User, Comment
from connect import engine


print("CREATING TABLES >>>> ")

# define a metadata then attach all database tables you created onto that metadata object
# Bind the engine to metadata
Base.metadata.create_all(bind=engine)