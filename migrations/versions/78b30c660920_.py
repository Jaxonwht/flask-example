"""empty message

Revision ID: 78b30c660920
Revises:
Create Date: 2021-03-07 18:10:33.205936

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "78b30c660920"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "results",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("result_all", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column("result_no_stop_words", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("results")
    # ### end Alembic commands ###
