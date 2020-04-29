"""updated user to have password

Revision ID: d28695820632
Revises: 2da2db9852df
Create Date: 2020-04-29 15:11:45.126340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd28695820632'
down_revision = '2da2db9852df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###