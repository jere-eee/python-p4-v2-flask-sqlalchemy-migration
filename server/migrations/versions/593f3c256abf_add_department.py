"""add Department

Revision ID: 593f3c256abf
Revises: 9a99885ce8e4
Create Date: 2025-01-13 15:09:25.787828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '593f3c256abf'
down_revision = '9a99885ce8e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
