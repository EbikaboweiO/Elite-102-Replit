from website import create_app

#creates the app
app = create_app() 

#runs the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)