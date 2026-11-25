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


class ExamResults(Base):
    __tablename__ = 'exam_results'
    __table_args__ = (
        CheckConstraint('marks_obtained <= maximum_marks', name='exam_results_check'),
        CheckConstraint('marks_obtained >= 0::numeric', name='exam_results_marks_obtained_check'),
        CheckConstraint('maximum_marks > 0::numeric', name='exam_results_maximum_marks_check'),
        ForeignKeyConstraint(['school_id', 'enrollment_id'], ['enrollments.school_id', 'enrollments.id'], name='exam_results_school_id_enrollment_id_fkey'),
        ForeignKeyConstraint(['school_id', 'exam_id'], ['exams.school_id', 'exams.id'], name='exam_results_school_id_exam_id_fkey'),
        ForeignKeyConstraint(['school_id', 'subject_id'], ['subjects.school_id', 'subjects.id'], name='exam_results_school_id_subject_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='exam_results_school_id_fkey'),
        PrimaryKeyConstraint('id', name='exam_results_pkey'),
        UniqueConstraint('school_id', 'exam_id', 'enrollment_id', 'subject_id', name='exam_results_school_id_exam_id_enrollment_id_subject_id_key'),
        Index('idx_exam_results_exam', 'school_id', 'exam_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    exam_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    enrollment_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    subject_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    marks_obtained: Mapped[decimal.Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    maximum_marks: Mapped[decimal.Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(String(10))
    remarks: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    enrollments: Mapped['Enrollments'] = relationship('Enrollments', back_populates='exam_results')
    exams: Mapped['Exams'] = relationship('Exams', back_populates='exam_results')
    subjects: Mapped['Subjects'] = relationship('Subjects', back_populates='exam_results')
    school: Mapped['Schools'] = relationship('Schools', back_populates='exam_results')
