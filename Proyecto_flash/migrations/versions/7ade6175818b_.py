"""empty message

Revision ID: 7ade6175818b
Revises: 706f78532fc8
Create Date: 2021-02-09 19:14:14.809063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ade6175818b'
down_revision = '706f78532fc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user__payment__method')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user__payment__method',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('payment_method_code', sa.VARCHAR(length=10), nullable=True),
    sa.Column('credit_card_number', sa.INTEGER(), nullable=True),
    sa.Column('payment_method_details', sa.VARCHAR(length=500), nullable=True),
    sa.ForeignKeyConstraint(['payment_method_code'], ['ref_payment_method.payment_method_code'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
