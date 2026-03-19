from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/info")
def get_info():
    now = datetime.now()
    next_year = datetime(year=now.year + 1, month=1, day=1)
    delta = next_year - now

    return {
        "days_before_new_year": delta.days
    }