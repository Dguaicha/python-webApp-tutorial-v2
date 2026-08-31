import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

db_connection_string = os.getenv("DB_CONNECTION_STRING")

ca_cert_path = r"C:/Users/dguai/Downloads/isrgrootx1.pem"

engine = create_engine(db_connection_string, connect_args={"ssl": {"ca": ca_cert_path}})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))

        return jobs
