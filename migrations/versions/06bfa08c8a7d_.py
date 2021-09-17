"""empty message

Revision ID: 06bfa08c8a7d
Revises: f75d5cb9d83b
Create Date: 2021-09-02 10:37:58.752230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06bfa08c8a7d'
down_revision = 'f75d5cb9d83b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alertaplaca', sa.String(), nullable=True),
    sa.Column('alertaselector', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comunication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('selector', sa.String(), nullable=True),
    sa.Column('flag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.String(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('comunication')
    op.drop_table('alert')
    # ### end Alembic commands ###