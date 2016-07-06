"""empty message

Revision ID: 3771f5ffc257
Revises: None
Create Date: 2016-07-06 10:19:52.641002

"""

# revision identifiers, used by Alembic.
revision = '3771f5ffc257'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=500), nullable=True),
    sa.Column('location', sa.String(length=500), nullable=True),
    sa.Column('logo', sa.String(length=500), nullable=True),
    sa.Column('title', sa.String(length=500), nullable=True),
    sa.Column('category', sa.String(length=120), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('requirement', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.String(length=200), nullable=True),
    sa.Column('contract_type', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    ### end Alembic commands ###
