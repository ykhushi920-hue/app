"""empty message

Revision ID: 552d735a2f1f
Revises: 1759f73274ee
Create Date: 2020-05-15 16:33:23.558895

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '552d735a2f1f'
down_revision = '1759f73274ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('alias_mailbox_user_id_fkey', 'alias_mailbox', type_='foreignkey')
    op.drop_column('alias_mailbox', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alias_mailbox', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('alias_mailbox_user_id_fkey', 'alias_mailbox', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
