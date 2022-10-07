import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from core.database import metadata

link_table = sa.Table(
    'link',
    metadata,
    sa.Column(
        'short_link',
        sa.String(255),
        primary_key=True,
        unique=True,
        index=True,
        nullable=False,
    ),
    sa.Column(
        'full_link',
        sa.String(2083),
        index=True,
        nullable=False,
    ),
    sa.Column(
        'created_at',
        sa.DateTime(True),
        nullable=False,
        server_default=sa.func.now(),
    ),
)
