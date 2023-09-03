from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import root_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    title: str
    id: int
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass
