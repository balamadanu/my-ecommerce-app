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


class AcademicYears(Base):
    __tablename__ = 'academic_years'
    __table_args__ = (
        CheckConstraint('end_date > start_date', name='academic_years_check'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='academic_years_school_id_fkey'),
        PrimaryKeyConstraint('id', name='academic_years_pkey'),
        UniqueConstraint('school_id', 'id', name='academic_years_school_id_id_key'),
        UniqueConstraint('school_id', 'name', name='academic_years_school_id_name_key'),
        Index('uq_current_academic_year', 'school_id', postgresql_where='(is_current = true)', unique=True)
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_current: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    school: Mapped['Schools'] = relationship('Schools', back_populates='academic_years')
    exams: Mapped[list['Exams']] = relationship('Exams', back_populates='academic_years')
    fee_structures: Mapped[list['FeeStructures']] = relationship('FeeStructures', back_populates='academic_years')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='academic_years')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='academic_years')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='academic_years')
