"""empty message

Revision ID: a89a143735e5
Revises: f1531223b9e5
Create Date: 2016-07-24 15:10:24.786000

"""

# revision identifiers, used by Alembic.
revision = 'a89a143735e5'
down_revision = 'f1531223b9e5'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('call_for_papers', sa.Column('timezone', sa.String(), nullable=False))
    op.alter_column('events', 'has_session_speakers',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_column('session', 'timezone')
    op.drop_column('session_version', 'timezone')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session_version', sa.Column('timezone', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('session', sa.Column('timezone', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('events', 'has_session_speakers',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('call_for_papers', 'timezone')
    ### end Alembic commands ###
