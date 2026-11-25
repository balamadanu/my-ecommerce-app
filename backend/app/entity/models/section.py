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


class Sections(Base):
    __tablename__ = 'sections'
    __table_args__ = (
        CheckConstraint('capacity IS NULL OR capacity > 0', name='sections_capacity_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='sections_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_id'], ['classes.school_id', 'classes.id'], name='sections_school_id_class_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_teacher_id'], ['teachers.school_id', 'teachers.id'], name='sections_school_id_class_teacher_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='sections_school_id_fkey'),
        PrimaryKeyConstraint('id', name='sections_pkey'),
        UniqueConstraint('school_id', 'class_id', 'academic_year_id', 'name', name='sections_school_id_class_id_academic_year_id_name_key'),
        UniqueConstraint('school_id', 'id', 'class_id', 'academic_year_id', name='sections_school_id_id_class_id_academic_year_id_key'),
        UniqueConstraint('school_id', 'id', name='sections_school_id_id_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    capacity: Mapped[Optional[int]] = mapped_column(Integer)
    class_teacher_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='sections')
    classes: Mapped['Classes'] = relationship('Classes', back_populates='sections')
    teachers: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='sections')
    school: Mapped['Schools'] = relationship('Schools', back_populates='sections')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='sections')
