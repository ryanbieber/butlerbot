"""Models."""

from enum import Enum
import pandera.polars as pa
from pandera.typing import Series
import datetime
from pydantic import BaseModel


class Tags(str, Enum):
    """
    Enum for categorizing resources with tags.

    Attributes:
        appointment: Represents an appointment-related tag.
        personal: Represents a personal-related tag.
        work: Represents a work-related tag.
        fun_fact: Represents a fun fact-related tag.
        todo: Represents a to-do-related tag.
        misc: Represents a miscellaneous-related tag.
    """

    APPOINTMENT = "appointment"
    PERSONAL = "personal"
    WORK = "work"
    FUN_FACT = "fun_fact"
    TODO = "todo"
    MISC = "misc"


class Note(BaseModel):
    """
    Schema for a note.

    Args:
        id (int): Unique identifier for the note.
        tags (Tags): Tags associated with the note.
        content (str): Content of the note.
        created_at (datetime.date): Date when the note was created.
        date (datetime.date): Date when the note was added.

    """

    id: int
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
        tags (Series[Tags]): Tags associated with the note.
        content (Series[str]): Content of the note.
        created_at (Series[datetime.date]): Date when the note was created.
        date (Series[datetime.date]): Date when the note was added.

    """

    id: Series[int] = pa.Field(nullable=False)
    tags: Series[Tags] = pa.Field(nullable=False)
    content: Series[str] = pa.Field(nullable=False)
    created_at: Series[datetime.date] = pa.Field(nullable=False)
    date: Series[datetime.date] = pa.Field(nullable=False)

    class Config:
        coerce = True
