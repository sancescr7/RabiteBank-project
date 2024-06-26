"""empty message

Revision ID: dfc3540773ab
Revises: 
Create Date: 2024-05-31 20:14:25.961548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfc3540773ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaniya',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.Column('baslama', sa.String(length=100), nullable=False),
    sa.Column('bitme', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emanetler',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('muddet', sa.Integer(), nullable=False),
    sa.Column('faiz', sa.Float(), nullable=False),
    sa.Column('valyuta', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('emanetler_sorgu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Radio', sa.String(length=100), nullable=False),
    sa.Column('Name', sa.String(length=100), nullable=False),
    sa.Column('Sorname', sa.String(length=100), nullable=False),
    sa.Column('Phone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('scrool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cash', sa.Integer(), nullable=False),
    sa.Column('gracePeriod', sa.Integer(), nullable=False),
    sa.Column('CardMin', sa.Integer(), nullable=False),
    sa.Column('CardMax', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('sorgu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Branch', sa.String(length=100), nullable=False),
    sa.Column('Service', sa.String(length=100), nullable=False),
    sa.Column('Date', sa.String(length=100), nullable=False),
    sa.Column('Time', sa.String(length=100), nullable=False),
    sa.Column('Phone', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('xeberler',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('data', sa.String(length=100), nullable=False),
    sa.Column('catecory', sa.String(length=100), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('xeberler')
    op.drop_table('user')
    op.drop_table('sorgu')
    op.drop_table('scrool')
    op.drop_table('emanetler_sorgu')
    op.drop_table('emanetler')
    op.drop_table('campaniya')
    # ### end Alembic commands ###
