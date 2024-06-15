"""add more columns

Revision ID: 67dfd64eadbe
Revises: 76743510d66c
Create Date: 2024-06-13 20:44:59.257105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '67dfd64eadbe'
down_revision: Union[str, None] = '76743510d66c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news_articles', sa.Column('description', sa.Text(), nullable=True))
    op.add_column('news_articles', sa.Column('publishedAt', sa.DateTime(), nullable=True))
    op.add_column('news_articles', sa.Column('url', sa.Text(), nullable=True))
    op.add_column('news_articles', sa.Column('urlToImage', sa.Text(), nullable=True))
    op.drop_column('news_articles', 'published_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news_articles', sa.Column('published_at', mysql.DATETIME(), nullable=True))
    op.drop_column('news_articles', 'urlToImage')
    op.drop_column('news_articles', 'url')
    op.drop_column('news_articles', 'publishedAt')
    op.drop_column('news_articles', 'description')
    # ### end Alembic commands ###
