# Main file to run the application
from todol import create_app

# Returns the entire app with the Flask configuration
if __name__ == '__main__':
  app = create_app()
  app.run()