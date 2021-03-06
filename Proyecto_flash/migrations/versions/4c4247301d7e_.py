"""empty message

Revision ID: 4c4247301d7e
Revises: 96fc12469678
Create Date: 2021-02-09 15:36:07.362988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4247301d7e'
down_revision = '96fc12469678'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
