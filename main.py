from fastapi import FastAPI
from scraper import get_app_genres
from types_lib.scraper_types import ScraperInputType, GenresResponse, GenresRequest

app = FastAPI()


@app.post("/genres", response_model=GenresResponse)
def genres(request: GenresRequest):
    input_data = ScraperInputType(apps=request.apps)
    results = get_app_genres(input_data)

    return GenresResponse(results=results)


# ---- run directly ----
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )