import databases
import sqlalchemy

from core.settings import POSTGRES_URL, POSTGRES_MIN_CONNECTIONS_SIZE, POSTGRES_MAX_CONNECTIONS_SIZE

metadata = sqlalchemy.MetaData()

database = databases.Database(
    POSTGRES_URL,
    min_size=POSTGRES_MIN_CONNECTIONS_SIZE,
    max_size=POSTGRES_MAX_CONNECTIONS_SIZE,
    statement_cache_size=0,
)
