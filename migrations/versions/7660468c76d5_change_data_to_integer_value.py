"""change data to integer value

Revision ID: 7660468c76d5
Revises: 
Create Date: 2020-04-25 01:31:28.510911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7660468c76d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('virus_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('case_total', sa.Integer(), nullable=True),
    sa.Column('case_today', sa.Integer(), nullable=True),
    sa.Column('case_active', sa.Integer(), nullable=True),
    sa.Column('case_serious', sa.Integer(), nullable=True),
    sa.Column('recovered_total', sa.Integer(), nullable=True),
    sa.Column('death_today', sa.Integer(), nullable=True),
    sa.Column('death_total', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('virus_data')
    # ### end Alembic commands ###