from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from data.marvel_data import marvel_characters_db


app = FastAPI()

app.mount("/images", StaticFiles(directory="static/images"), name="images")


@app.get("/marvel_character/{name}", description="The 'name' must be lowercase.")
async def get_marvel_character_by_name(name: str):
    character = marvel_characters_db.get(name)
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return JSONResponse(content=character.dict(), status_code=200)
