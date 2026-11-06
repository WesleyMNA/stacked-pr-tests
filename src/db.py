"""A small in-memory database for storing dictionaries by table."""

from typing import Any


class InMemoryDatabase:
    """Store records in memory, grouped into named tables."""

    def __init__(self) -> None:
        self._tables: dict[str, list[dict[str, Any]]] = {}

    def select(
        self,
        table: str,
        filters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Return copies of records in *table* matching all provided filters."""
        records = self._tables.get(table, [])
        if filters is None:
            return [record.copy() for record in records]
        return [
            record.copy()
            for record in records
            if all(record.get(key) == value for key, value in filters.items())
        ]

    def create(self, table: str, record: dict[str, Any]) -> dict[str, Any]:
        """Add a record to *table* and return a copy of it."""
        stored_record = record.copy()
        self._tables.setdefault(table, []).append(stored_record)
        return stored_record.copy()

    def delete(
        self,
        table: str,
        filters: dict[str, Any],
    ) -> int:
        """Delete records matching all filters and return the number removed."""
        records = self._tables.get(table, [])
        remaining = [
            record
            for record in records
            if not all(record.get(key) == value for key, value in filters.items())
        ]
        deleted_count = len(records) - len(remaining)
        self._tables[table] = remaining
        return deleted_count
