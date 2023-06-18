"""empty message

Revision ID: e1ce6427bf39
Revises: 45917e595576
Create Date: 2023-06-18 15:02:54.863683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ce6427bf39'
down_revision = '45917e595576'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('studen_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('semestre', sa.String(length=80), nullable=False),
    sa.Column('materias', sa.String(length=80), nullable=False),
    sa.Column('codigo', sa.Integer(), nullable=False),
    sa.Column('prelaciones', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('codigo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('studen_subject')
    # ### end Alembic commands ###
