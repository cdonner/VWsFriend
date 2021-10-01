"""Added fields for real kwh and cost

Revision ID: 023aa9f36740
Revises: 184bb7a71ada
Create Date: 2021-09-28 16:24:00.035078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '023aa9f36740'
down_revision = '184bb7a71ada'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('charging_sessions', sa.Column('realCharged_kWh', sa.Float(), nullable=True))
    op.add_column('charging_sessions', sa.Column('realCost_ct', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('charging_sessions', 'realCost_ct')
    op.drop_column('charging_sessions', 'realCharged_kWh')
    # ### end Alembic commands ###