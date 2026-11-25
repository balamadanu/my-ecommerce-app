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


class Exams(Base):
    __tablename__ = 'exams'
    __table_args__ = (
        CheckConstraint('start_date IS NULL OR end_date IS NULL OR end_date >= start_date', name='exams_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='exams_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_id'], ['classes.school_id', 'classes.id'], name='exams_school_id_class_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='exams_school_id_fkey'),
        PrimaryKeyConstraint('id', name='exams_pkey'),
        UniqueConstraint('school_id', 'id', name='exams_school_id_id_key'),
        Index('idx_exams_academic_year', 'school_id', 'academic_year_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    exam_type: Mapped[Optional[str]] = mapped_column(String(50))
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='exams')
    classes: Mapped['Classes'] = relationship('Classes', back_populates='exams')
    school: Mapped['Schools'] = relationship('Schools', back_populates='exams')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='exams')
