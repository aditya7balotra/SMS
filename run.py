from app import createApp

# creating the flask app
app = createApp()


# run the app
if __name__ == '__main__':
    app.run(
        debug= True
    )