"""empty message

Revision ID: b3c1f446535d
Revises: a589976d12e3
Create Date: 2024-08-09 14:45:16.744028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c1f446535d'
down_revision: Union[str, None] = 'a589976d12e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
