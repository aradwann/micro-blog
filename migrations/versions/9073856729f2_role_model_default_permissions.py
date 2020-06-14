"""Role model default, permissions

Revision ID: 9073856729f2
Revises: 1953fd481948
Create Date: 2020-06-14 17:29:46.755239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9073856729f2'
down_revision = '1953fd481948'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
