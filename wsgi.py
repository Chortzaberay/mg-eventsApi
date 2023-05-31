from src import create_app
from config import configs


app = create_app(configs['dev'])



if __name__ == "__main__":
    app.run(debug=True)