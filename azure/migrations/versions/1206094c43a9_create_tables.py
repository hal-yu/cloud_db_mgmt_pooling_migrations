"""create tables

Revision ID: 1206094c43a9
Revises: 
Create Date: 2023-10-28 00:08:54.158878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1206094c43a9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('phone_number', sa.String(length=15), nullable=True))
    op.add_column('patients', sa.Column('gender', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'gender')
    op.drop_column('patients', 'phone_number')
    # ### end Alembic commands ###