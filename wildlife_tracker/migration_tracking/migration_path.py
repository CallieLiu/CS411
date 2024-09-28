from typing import Optional

class MigrationPath:

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def get_migrations() -> list[Migration]:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass
    