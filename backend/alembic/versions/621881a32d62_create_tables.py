"""Create tables.

Revision ID: 621881a32d62
Revises: 
Create Date: 2019-12-22 17:15:52.046161

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "621881a32d62"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("full_name", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.Column("is_superuser", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_index(op.f("ix_user_full_name"),
                    "user", ["full_name"],
                    unique=False)
    op.create_index(op.f("ix_user_id"), "user", ["id"], unique=False)
    op.create_table(
        "submission",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("survey_service_type", sa.String(), nullable=True),
        sa.Column("survey_outages", sa.String(), nullable=True),
        sa.Column("survey_disruptions", sa.String(), nullable=True),
        sa.Column("survey_subscribe_upload", sa.String(), nullable=True),
        sa.Column("survey_subscribe_download", sa.String(), nullable=True),
        sa.Column("survey_bundle", sa.String(), nullable=True),
        sa.Column("survey_current_cost", sa.String(), nullable=True),
        sa.Column("survey_satisfaction", sa.String(), nullable=True),
        sa.Column("survey_carrier_choice", sa.String(), nullable=True),
        sa.Column("survey_story", sa.String(), nullable=True),
        sa.Column("survey_email", sa.String(), nullable=True),
        sa.Column("survey_phone", sa.String(), nullable=True),
        sa.Column("actual_download", sa.Integer(), nullable=True),
        sa.Column("actual_upload", sa.Integer(), nullable=True),
        sa.Column("min_rtt", sa.Integer(), nullable=True),
        sa.Column("latitude", sa.Numeric(), nullable=True),
        sa.Column("longitude", sa.Numeric(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_submission_id"),
                    "submission", ["id"],
                    unique=False)
    op.create_index(op.f("ix_submission_survey_email"),
                    "submission", ["survey_email"],
                    unique=False)
    op.create_index(op.f("ix_submission_survey_phone"),
                    "submission", ["survey_phone"],
                    unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_submission_survey_phone"), table_name="submission")
    op.drop_index(op.f("ix_submission_survey_email"), table_name="submission")
    op.drop_index(op.f("ix_submission_id"), table_name="submission")
    op.drop_table("submission")
    op.drop_index(op.f("ix_user_id"), table_name="user")
    op.drop_index(op.f("ix_user_full_name"), table_name="user")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
