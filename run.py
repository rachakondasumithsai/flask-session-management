from project import create_app

flaskapp = create_app()
if __name__ == '__main__':
    flaskapp.run(debug=True)