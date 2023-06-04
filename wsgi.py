from src import create_app
from config import configs
import os 


app = create_app(configs[os.environ.get("CONFIG", "dev")])



if __name__ == "__main__":
    app.run(debug=True)