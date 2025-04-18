"""mapping added

Revision ID: 91bff2935265
Revises: 01e6da0739e5
Create Date: 2025-04-16 14:07:27.903661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91bff2935265'
down_revision: Union[str, None] = '01e6da0739e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'categories', 'categories', ['parent_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='foreignkey')
    # ### end Alembic commands ###
