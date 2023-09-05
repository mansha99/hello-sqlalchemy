"""create planet table

Revision ID: 4c2eb4fe9aa5
Revises: 
Create Date: 2023-09-05 11:56:56.419497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c2eb4fe9aa5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
           'planet',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(50), nullable=False),
    )


def downgrade() -> None:
    pass
