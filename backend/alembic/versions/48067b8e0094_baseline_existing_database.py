"""baseline existing database

Revision ID: 48067b8e0094
Revises: e605cb558578
Create Date: 2026-11-25 16:24:38.959379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48067b8e0094'
down_revision: Union[str, Sequence[str], None] = 'e605cb558578'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
