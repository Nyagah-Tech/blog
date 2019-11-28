"""create user pass_code column

Revision ID: a19652c237ee
Revises: 603d11b95ca2
Create Date: 2019-11-28 21:23:32.505809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a19652c237ee'
down_revision = '603d11b95ca2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_code', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_code')
    # ### end Alembic commands ###