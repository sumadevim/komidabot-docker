"""Allow closing days to not have an end date

Revision ID: bc1ef0083bb4
Revises: 9b9afdcf4e4e
Create Date: 2020-09-22 18:29:49.798217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1ef0083bb4'
down_revision = '9b9afdcf4e4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('closing_days', 'last_day',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('closing_days', 'last_day',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
