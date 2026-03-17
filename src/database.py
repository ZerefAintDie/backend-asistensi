from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/acara-rsi"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session