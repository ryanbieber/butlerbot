"""Storage Module."""

import os
from pathlib import Path
from models import Note, NotesTable
import polars as pl
import structlog

DATA_PATH = Path(__file__).resolve().parent.parent / "data"


logger = structlog.get_logger(__name__)


def save_note_to_file(note: Note) -> None:
    """Save a note to a file."""
    # read in old notes file
    notes_file = DATA_PATH / "notes.parquet"
    if os.path.exists(notes_file):
        logger.info(f"Reading old notes from {notes_file}")
        old_notes = pl.read_parquet(notes_file)
        # append new notes to old notes
        max_id = old_notes.select(pl.col("id")).max()
    else:
        logger.info(f"Creating new notes file at {notes_file}")
        old_notes = pl.DataFrame()
        max_id = 0
    df = pl.DataFrame(note.model_dump()).with_columns(id=pl.lit(max_id + 1))
    validated_df = NotesTable.validate(df)
    combined_notes = pl.concat([old_notes, validated_df])
    # write to file
    combined_notes.write_parquet(notes_file, compression="lz4")
    logger.info(f"Saved note to {notes_file}")


def get_notes() -> pl.DataFrame:
    """Get all notes."""
    notes_file = DATA_PATH / "notes.parquet"
    if os.path.exists(notes_file):
        logger.info(f"Reading notes from {notes_file}")
        notes = pl.read_parquet(notes_file)
        return NotesTable.validate(notes)
    else:
        logger.info(f"No notes found at {notes_file}")
        return pl.DataFrame()
