"""Add other_ fields only

Revision ID: 67440e3569d3
Revises: 01eaaac36a50
Create Date: 2025-05-12 11:35:05.845245
"""

from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '67440e3569d3'
down_revision: Union[str, None] = '01eaaac36a50'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('field_submissions', sa.Column('other_irrigation_method', sa.String(), nullable=True))
    op.add_column('field_submissions', sa.Column('other_animal_type', sa.String(), nullable=True))
    op.add_column('field_submissions', sa.Column('other_implement_used', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('field_submissions', 'other_irrigation_method')
    op.drop_column('field_submissions', 'other_animal_type')
    op.drop_column('field_submissions', 'other_implement_used')
