from pydantic import BaseModel
from typing import Optional


class MarvelCharater(BaseModel):
    name: str
    alias: str
    real_name: str
    short_bio: str
    first_appearance: int
    is_villian: Optional[bool] = None
    image_url: str

    def dict(self, *args, **kwargs):
        return super().dict(*args, **kwargs, exclude_none=True)