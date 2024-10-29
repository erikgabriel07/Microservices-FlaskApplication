from settings.flask_app import create_app

def main():
    app = create_app()
    app.run('127.0.0.1', port=5000, debug=True) # debug somente em desenvolvimento


if __name__ == '__main__':
    main()