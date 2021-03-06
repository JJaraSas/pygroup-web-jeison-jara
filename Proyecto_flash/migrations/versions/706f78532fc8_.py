"""empty message

Revision ID: 706f78532fc8
Revises: 6ed0bd0d3276
Create Date: 2021-02-09 19:02:38.418538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '706f78532fc8'
down_revision = '6ed0bd0d3276'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ref__payment__method')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ref__payment__method',
    sa.Column('payment_method_code', sa.VARCHAR(length=10), nullable=False),
    sa.Column('payment_method_description', sa.VARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('payment_method_code')
    )
    # ### end Alembic commands ###
