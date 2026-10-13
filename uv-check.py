import sys, platform, sqlite3
from importlib.metadata import version, PackageNotFoundError

print("uv-managed Python:", sys.executable)
print("python            ", platform.python_version())
print("sqlite (stdlib)   ", sqlite3.sqlite_version)
for pkg in ("duckdb", "datasette", "sqlite-utils", "pydantic", "sqlalchemy"):
    try:
        print(f"{pkg:18s}", version(pkg))
    except PackageNotFoundError:
        print(f"{pkg:18s}", "NOT INSTALLED")