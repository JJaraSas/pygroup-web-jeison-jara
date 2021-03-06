"""empty message

Revision ID: 04790b0b3961
Revises: 7ade6175818b
Create Date: 2021-02-10 09:11:27.066660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04790b0b3961'
down_revision = '7ade6175818b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ref_order_status_code') as batch_op:
        batch_op.drop_column('invoice_status_decription')
        batch_op.drop_column('invoice_status_code')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ref_order_status_code', sa.Column('invoice_status_code', sa.INTEGER(), nullable=False))
    op.add_column('ref_order_status_code', sa.Column('invoice_status_decription', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('ref_order_status_code', 'order_status_decription')
    op.drop_column('ref_order_status_code', 'order_status_code')
    # ### end Alembic commands ###
