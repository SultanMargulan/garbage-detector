"""empty message

Revision ID: f982952e8bd9
Revises: 273797912830
Create Date: 2025-03-17 06:02:46.607450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f982952e8bd9'
down_revision = '273797912830'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('detection', schema=None) as batch_op:
        batch_op.create_index('idx_image_path', ['image_path'], unique=False)
        batch_op.create_index('idx_session', ['session_id'], unique=False)
        batch_op.create_index('idx_timestamp', ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('detection', schema=None) as batch_op:
        batch_op.drop_index('idx_timestamp')
        batch_op.drop_index('idx_session')
        batch_op.drop_index('idx_image_path')

    # ### end Alembic commands ###
