"""create user pass_code column

Revision ID: 603d11b95ca2
Revises: caf240851564
Create Date: 2019-11-28 16:41:21.236954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '603d11b95ca2'
down_revision = 'caf240851564'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
