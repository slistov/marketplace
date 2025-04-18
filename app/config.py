import os

DBUSER = os.getenv("DBUSER", "postgres")
DBPASSWORD = os.getenv("DBPASSWORD")
DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")

DATABASE_URL = f"postgresql+asyncpg://{DBUSER}:{DBPASSWORD}@{DBHOST}/{DBNAME}"
