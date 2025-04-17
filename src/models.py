"""Models."""

from enum import Enum
import pandera.polars as pa
from pandera.typing import Series
import datetime
from pydantic import BaseModel

class Created(Enum):
    """
    Enum representing the created status of a resource.
    """
    weather = "weather"
    calendar = "calendar"
    telegram = "telegram"
    personal = "personal"
    usps = "usps"
    ups = "ups"
    fedex = "fedex"
    amazon = "amazon"


class Tags(Enum):
    """
    Enum representing the tags used for categorizing resources.
    """
    weather = "weather"
    calendar = "calendar"
    telegram = "telegram"
    personal = "personal"
    mail = "mail"



class Note(BaseModel):
    """
    Schema for a note.

    Args:
        id (int): Unique identifier for the note.
        created (Created): The source of the note.
        tags (Tags): Tags associated with the note.
        content (str): Content of the note.
        created_at (datetime.date): Date when the note was created.
        date (datetime.date): Date when the note was added.

    """
    id: int
    created: Created
    tags: Tags
    content: str
    created_at: datetime.date
    date: datetime.date

    class Config:
        """
        Configuration for the Pydantic model.
        """
        use_enum_values = True
        arbitrary_types_allowed = True
        
        
class NotesTable(pa.DataFrameModel):
    """
    Schema for the notes table.

    Args:
        id (Series[int]): Unique identifier for the note.
        created (Series[Created]): The source of the note.
        tags (Series[Tags]): Tags associated with the note.
        content (Series[str]): Content of the note.
        created_at (Series[datetime.date]): Date when the note was created.
        date (Series[datetime.date]): Date when the note was added.

    """
    id: Series[int] = pa.Field(nullable=False)
    created: Series[Created] = pa.Field(nullable=False)
    tags: Series[Tags] = pa.Field(nullable=False)
    content: Series[str] = pa.Field(nullable=False)
    created_at: Series[datetime.date] = pa.Field(nullable=False)
    date: Series[datetime.date] = pa.Field(nullable=False)
