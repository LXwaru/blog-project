"""empty message

Revision ID: ef7c6a257195
Revises: d8fdc4dd2a33
Create Date: 2024-08-01 00:07:11.579126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef7c6a257195'
down_revision: Union[str, None] = 'd8fdc4dd2a33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
