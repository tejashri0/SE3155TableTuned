from urllib.parse import quote_plus

class Settings:
    db_user = "sandwich_user"
    db_password = "Sandwich123!"
    db_host = "localhost"
    db_port = "3306"
    db_name = "restaurant_db"

    # Properly URL-encode the password
    SQLALCHEMY_DATABASE_URL = (
        f"mysql+pymysql://{db_user}:{quote_plus(db_password)}@{db_host}:{db_port}/{db_name}?charset=utf8mb4"
    )

    app_host = "127.0.0.1"
    app_port = 8000

conf = Settings()
