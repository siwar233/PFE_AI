"""Initial migration.

Revision ID: da6ee73f0526
Revises: 
Create Date: 2024-05-29 18:21:57.946976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'da6ee73f0526'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('Experience')
    op.drop_table('Project')
    op.drop_table('Language')
    op.drop_table('JobApplication')
    op.drop_table('User')
    op.drop_table('CandidateLanguage')
    op.drop_table('Certification')
    op.drop_table('Education')
    op.drop_table('Resume')
    op.drop_table('Job')
    op.drop_table('Skill')
    op.drop_table('CandidateSkill')
    op.drop_table('Candidate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Candidate',
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone_num', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('adress', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('date_of_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIME(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIME(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('candidate_id', name='candidate_pkey'),
    sa.UniqueConstraint('email', name='email'),
    postgresql_ignore_search_path=False
    )
    op.create_table('CandidateSkill',
    sa.Column('candidate_skill_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('skill_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='CandidateSkill_candidate_id_fkey'),
    sa.ForeignKeyConstraint(['skill_id'], ['Skill.skill_id'], name='CandidateSkill_skill_id_fkey'),
    sa.PrimaryKeyConstraint('candidate_skill_id', name='CandidateSkill_pkey')
    )
    op.create_table('Skill',
    sa.Column('skill_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('skill_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('skill_id', name='Skill_pkey')
    )
    op.create_table('Job',
    sa.Column('job_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hr_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('job_title', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('job_description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('requirements', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('location', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('salary_range', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('posted_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('closing_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['hr_id'], ['HR.hr_id'], name='Job_hr_id_fkey'),
    sa.PrimaryKeyConstraint('job_id', name='Job_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Resume',
    sa.Column('resume_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('resume_file', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('uploaded_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('parsed_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='pk2'),
    sa.PrimaryKeyConstraint('resume_id', name='Resume_pkey')
    )
    op.create_table('Education',
    sa.Column('education_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('degree', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('institution_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('field_of_study', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='Education_candidate_id_fkey'),
    sa.PrimaryKeyConstraint('education_id', name='Education_pkey')
    )
    op.create_table('Certification',
    sa.Column('certification_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('certification_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('issuing_organization', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('issue_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('expiration_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='Certification_candidate_id_fkey'),
    sa.PrimaryKeyConstraint('certification_id', name='Certification_pkey')
    )
    op.create_table('CandidateLanguage',
    sa.Column('candidate_language_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('language_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('proficiency_level', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='CandidateLanguage_candidate_id_fkey'),
    sa.ForeignKeyConstraint(['language_id'], ['Language.language_id'], name='CandidateLanguage_language_id_fkey'),
    sa.PrimaryKeyConstraint('candidate_language_id', name='CandidateLanguage_pkey')
    )
    op.create_table('User',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='User_pkey')
    )
    op.create_table('JobApplication',
    sa.Column('job_application_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('job_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('application_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='pk1'),
    sa.ForeignKeyConstraint(['job_id'], ['Job.job_id'], name='pk2'),
    sa.PrimaryKeyConstraint('job_application_id', name='JobApplication_pkey')
    )
    op.create_table('Language',
    sa.Column('language_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('language_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('language_id', name='Language_pkey')
    )
    op.create_table('Project',
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('project_title', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('project_description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('technologies', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='pk3'),
    sa.PrimaryKeyConstraint('project_id', name='Project_pkey')
    )
    op.create_table('Experience',
    sa.Column('experience_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('candidate_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('job_title', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('company_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('stard_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('end_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('job_description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['candidate_id'], ['Candidate.candidate_id'], name='Experience_candidate_id_fkey'),
    sa.PrimaryKeyConstraint('experience_id', name='Experience_pkey')
    )
    op.create_table('HR',
    sa.Column('hr_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone_num', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.ARRAY(postgresql.TIME(timezone=True)), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIME(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('hr_id', name='HR_pkey')
    )
    op.drop_table('user')
    # ### end Alembic commands ###