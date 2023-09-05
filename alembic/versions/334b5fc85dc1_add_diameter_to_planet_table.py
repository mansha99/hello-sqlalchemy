"""add diameter to  planet table

Revision ID: 334b5fc85dc1
Revises: 4c2eb4fe9aa5
Create Date: 2023-09-05 11:57:34.158927

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '334b5fc85dc1'
down_revision: Union[str, None] = '4c2eb4fe9aa5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('planet', sa.Column('diameter', sa.Float()))


def downgrade() -> None:
    pass
