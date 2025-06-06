"""Recreate schema after cleanup

Revision ID: 8c480264b90a
Revises: 
Create Date: 2025-05-12 11:26:49.831170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8c480264b90a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_submissions_geolocation', table_name='submissions', postgresql_using='gist')
    op.drop_index('ix_submissions_id', table_name='submissions')
    op.drop_index('ix_submissions_odk_id', table_name='submissions')
    op.drop_table('submissions')
    op.drop_table('enrollment_dates')
    op.drop_index('ix_field_submissions_Farmer_unique_code', table_name='field_submissions')
    op.drop_index('ix_field_submissions_display_field_id', table_name='field_submissions')
    op.drop_index('ix_field_submissions_id', table_name='field_submissions')
    op.drop_table('field_submissions')
    op.drop_table('spatial_ref_sys')
    op.drop_table('practice_submissions')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('practice_submissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('farmer_unique_code', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('display_field_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('growing_year', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planting_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('production_volume', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('residue_harvested', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('residue_burned', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('residue_shredded', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('residue_shredded_fuel', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('other_residue_shredded_fuel', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('residue_shredded_usage', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('number_of_events', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('type_of_event', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('date_land', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('power_by_land', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('other_power_by', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('fuel_usage_litres', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('hours_of_animal_tillage', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('number_of_irrigation_events', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('animal_ploughing', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('electricity_bill', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('enrollment_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='practice_submissions_pkey')
    )
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('srid > 0 AND srid <= 998999', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    op.create_table('field_submissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('submission_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Farmer_unique_code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('display_field_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Enrollment_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('shape_area_note', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('Number_of_irrigation_events', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('hours_of_animal_tillage', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('state_IPs', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('Implementing_partner_s', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['submission_id'], ['submissions.id'], name='field_submissions_submission_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='field_submissions_pkey')
    )
    op.create_index('ix_field_submissions_id', 'field_submissions', ['id'], unique=False)
    op.create_index('ix_field_submissions_display_field_id', 'field_submissions', ['display_field_id'], unique=False)
    op.create_index('ix_field_submissions_Farmer_unique_code', 'field_submissions', ['Farmer_unique_code'], unique=False)
    op.create_table('enrollment_dates',
    sa.Column('farmer_unique_code', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('enrollment_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('farmer_unique_code', name='enrollment_dates_pkey')
    )
    op.create_table('submissions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('odk_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('data', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('geolocation', sa.NullType(), autoincrement=False, nullable=True),
    sa.Column('farmer_photo', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='submissions_pkey')
    )
    op.create_index('ix_submissions_odk_id', 'submissions', ['odk_id'], unique=True)
    op.create_index('ix_submissions_id', 'submissions', ['id'], unique=False)
    op.create_index('idx_submissions_geolocation', 'submissions', ['geolocation'], unique=False, postgresql_using='gist')
    # ### end Alembic commands ###
