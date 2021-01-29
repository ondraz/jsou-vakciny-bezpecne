"""empty message

Revision ID: 0b655cf4ab16
Revises: 
Create Date: 2021-01-29 23:34:21.113103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b655cf4ab16'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat',
    sa.Column('date_from', sa.String(length=64), nullable=False),
    sa.Column('date_to', sa.String(length=64), nullable=False),
    sa.Column('vaccinated', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('date_from')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat')
    # ### end Alembic commands ###
