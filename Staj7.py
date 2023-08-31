import sqlite3
from fastapi import FastAPI,HTTPException,Query

app = FastAPI()
conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()
tutorial_db = [
    {"title": "Film1", "year": 1982},
    {"title": "Film2", "year": 1983},
    {"title": "Film3", "year": 1984},
]

@app.get("/movies", response_model=list[dict])
async def get_movies_by_year(year: int = Query(..., title="Yıl", description="Belirli bir yılda çıkan filmleri listele")):
    filtered_movies = [movie for movie in tutorial_db if movie["year"] == year]
    return filtered_movies

@app.get("/search", response_model=list[dict])
async def search_movies(title: str = Query(..., description="Search for movies by title")):
    cursor.execute("SELECT year, title FROM movie WHERE title LIKE ?", ('%' + title + '%',))
    movies = cursor.fetchall()
    movie_list = [{"year": row[0], "title": row[1]} for row in movies]
    return movie_list
