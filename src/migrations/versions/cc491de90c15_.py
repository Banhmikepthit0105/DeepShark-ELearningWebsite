"""empty message

Revision ID: cc491de90c15
Revises: d23ef3c7bc20
Create Date: 2025-02-16 15:11:53.721997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc491de90c15'
down_revision = 'd23ef3c7bc20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chat_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('history_chat_id', sa.Integer(), nullable=False),
    sa.Column('user_message', sa.Text(), nullable=False),
    sa.Column('bot_response', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['history_chat_id'], ['chat_history.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('question_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question_title', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('question_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('answer_1', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_1_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('answer_2', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_2_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('answer_3', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_3_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('answer_4', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_4_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('answer_5', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('answer_5_score', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('question_id', name='question_pkey')
    )
    op.create_table('history_chat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_message', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('bot_response', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='history_chat_pkey')
    )
    op.create_table('courses',
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('image', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.drop_table('chat_message')
    op.drop_table('chat_history')
    # ### end Alembic commands ###
