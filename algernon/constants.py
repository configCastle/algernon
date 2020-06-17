"""Constants for the project."""
import os

JWT_ALGORITHM = 'HS256'
JWT_SECRET = os.getenv('JWT_SECRET', 'secret')

mongo_port = 27017
standart_port = 8080
