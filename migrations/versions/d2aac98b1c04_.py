"""empty message

Revision ID: d2aac98b1c04
Revises: 9fa632f808f9
Create Date: 2019-08-21 20:52:40.933792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2aac98b1c04'
down_revision = '9fa632f808f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_constraint_commit', 'turn', type_='unique')
    op.create_unique_constraint('unique_constraint_commit', 'turn', ['number', 'match_id', 'hero_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_constraint_commit', 'turn', type_='unique')
    op.create_unique_constraint('unique_constraint_commit', 'turn', ['id', 'number', 'hero_id'])
    # ### end Alembic commands ###
