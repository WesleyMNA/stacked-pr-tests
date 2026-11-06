"""Service layer for working with the in-memory database."""

from typing import Any

from .db import InMemoryDatabase


class RecordService:
    """Provide record operations backed by an in-memory database."""

    def __init__(self, database: InMemoryDatabase, table: str) -> None:
        self._database = database
        self._table = table

    def select(self, filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        """Return records from this service's table, optionally filtered."""
        return self._database.select(self._table, filters)

    def create(self, record: dict[str, Any]) -> dict[str, Any]:
        """Create a record in this service's table."""
        return self._database.create(self._table, record)

    def delete(self, filters: dict[str, Any]) -> int:
        """Delete matching records and return the number removed."""
        return self._database.delete(self._table, filters)
