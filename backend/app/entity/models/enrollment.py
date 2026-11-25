from typing import Optional
import datetime
import decimal

from sqlalchemy import (
    BigInteger, Boolean, CheckConstraint, Date, DateTime,
    ForeignKeyConstraint, Identity, Index, Integer, Numeric,
    PrimaryKeyConstraint, String, Text, UniqueConstraint, text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Enrollments(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (
        CheckConstraint("status::text = ANY (ARRAY['active'::character varying, 'completed'::character varying, 'transferred'::character varying, 'withdrawn'::character varying]::text[])", name='enrollments_status_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='enrollments_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'section_id', 'class_id', 'academic_year_id'], ['sections.school_id', 'sections.id', 'sections.class_id', 'sections.academic_year_id'], name='enrollments_school_id_section_id_class_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'student_id'], ['students.school_id', 'students.id'], name='enrollments_school_id_student_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='enrollments_school_id_fkey'),
        PrimaryKeyConstraint('id', name='enrollments_pkey'),
        UniqueConstraint('school_id', 'id', name='enrollments_school_id_id_key'),
        UniqueConstraint('school_id', 'section_id', 'roll_number', name='enrollments_school_id_section_id_roll_number_key'),
        UniqueConstraint('school_id', 'student_id', 'academic_year_id', name='enrollments_school_id_student_id_academic_year_id_key'),
        Index('idx_enrollments_class', 'school_id', 'class_id', 'section_id'),
        Index('idx_enrollments_student', 'school_id', 'student_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    student_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    section_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    roll_number: Mapped[Optional[str]] = mapped_column(String(30))
    enrollment_date: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text('CURRENT_DATE'))
    status: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'active'::character varying"))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='enrollments')
    sections: Mapped['Sections'] = relationship('Sections', back_populates='enrollments')
    students: Mapped['Students'] = relationship('Students', back_populates='enrollments')
    school: Mapped['Schools'] = relationship('Schools', back_populates='enrollments')
    attendance: Mapped[list['Attendance']] = relationship('Attendance', back_populates='enrollments')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='enrollments')
