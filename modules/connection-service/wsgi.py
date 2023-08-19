import os
from app import initialize_app

app = initialize_app(os.getenv("FLASK_ENV") or "test")

if __name__ == "__main__":
    app.run(debug=True)
