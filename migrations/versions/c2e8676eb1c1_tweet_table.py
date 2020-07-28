"""tweet table

Revision ID: c2e8676eb1c1
Revises: 
Create Date: 2020-06-29 12:35:06.112080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e8676eb1c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweet',
    sa.Column('tID', sa.Integer(), nullable=False),
    sa.Column('given_text', sa.String(), nullable=False),
    sa.Column('selected_text', sa.String(), nullable=True),
    sa.Column('primary_sent', sa.Integer(), nullable=False),
    sa.Column('secondary_sent', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('tID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweet')
    # ### end Alembic commands ###