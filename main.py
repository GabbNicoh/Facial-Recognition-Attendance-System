from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# flask module not found ctrl + shit + p > python select interpreter to version