"""Terminal interface for the in-memory record service."""

from typing import Any

from src.db import InMemoryDatabase
from src.service import RecordService


def _read_record() -> dict[str, Any]:
    """Read a record as comma-separated key=value fields."""
    while True:
        raw = input("Fields (key=value, comma-separated): ").strip()
        record: dict[str, Any] = {}
        try:
            for field in raw.split(","):
                key, value = field.split("=", maxsplit=1)
                key = key.strip()
                if not key:
                    raise ValueError("Field names cannot be empty.")
                record[key] = value.strip()
            if record:
                return record
        except ValueError as error:
            print(f"Invalid record: {error}")
        print("Enter at least one field, such as name=Sam, role=admin.")


def run(service: RecordService) -> None:
    """Run the interactive terminal view for a record service."""
    actions = {
        "1": "List records",
        "2": "Create record",
        "3": "Delete records",
        "4": "Quit",
    }

    while True:
        print("\nRecord manager")
        for key, label in actions.items():
            print(f"{key}. {label}")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            records = service.select()
            if records:
                for index, record in enumerate(records, start=1):
                    print(f"{index}. {record}")
            else:
                print("No records found.")
        elif choice == "2":
            print(f"Created: {service.create(_read_record())}")
        elif choice == "3":
            key = input("Delete records where field equals: ").strip()
            if not key:
                print("Field name cannot be empty.")
                continue
            value = input("Value: ").strip()
            deleted = service.delete({key: value})
            print(f"Deleted {deleted} record(s).")
        elif choice == "4":
            print("Goodbye.")
            return
        else:
            print("Choose 1, 2, 3, or 4.")


def main() -> None:
    database = InMemoryDatabase()
    run(RecordService(database, "records"))


if __name__ == "__main__":
    main()
