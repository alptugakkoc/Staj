import sqlite3
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI()
con = sqlite3.connect("tutorial.db")
cursor = con.cursor()
class Movies (BaseModel):
    year: int
    title: str

@app.get("/movies", response_model=list[dict])
async def get_movies(year: int = Query(None, description="Filter movies by year")):
    if year is not None:
        cursor.execute("SELECT year, title FROM movie WHERE year = ? ORDER BY year", (year,))
    else:
        cursor.execute("SELECT year, title FROM movie ORDER BY year")
    movies = cursor.fetchall()
    movie_list = [{"year": title, "title": year} for year, title in movies]
    return movie_list

@app.post("/movies", response_model=Movies)
async def create_movie(movie: Movies):
    year = movie.year
    title = movie.title
    cursor.execute("INSERT INTO movie (year, title) VALUES (?, ?)", (year, title))
    con.commit()
    return {"year": year, "title": title}

@app.delete("/movies")
async def delete_movie(title: str, year: int):
    cursor.execute("DELETE FROM movie WHERE year = ? AND title = ?", (year, title))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": "Movie deleted successfully"}
