"""followers

Revision ID: 380fc06afc6d
Revises: 42465590f723
Create Date: 2023-10-26 16:21:24.195879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '380fc06afc6d'
down_revision = '42465590f723'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
