from web import app
import logging
from logging.handlers import RotatingFileHandler

if __name__ == "__main__":
    handler = RotatingFileHandler('instagredient.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
