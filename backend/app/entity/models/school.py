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


class Schools(Base):
    __tablename__ = 'schools'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='schools_pkey'),
        UniqueConstraint('code', name='schools_code_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(Text)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped[list['AcademicYears']] = relationship('AcademicYears', back_populates='school')
    classes: Mapped[list['Classes']] = relationship('Classes', back_populates='school')
    subjects: Mapped[list['Subjects']] = relationship('Subjects', back_populates='school')
    users: Mapped[list['Users']] = relationship('Users', back_populates='school')
    exams: Mapped[list['Exams']] = relationship('Exams', back_populates='school')
    fee_structures: Mapped[list['FeeStructures']] = relationship('FeeStructures', back_populates='school')
    parents: Mapped[list['Parents']] = relationship('Parents', back_populates='school')
    students: Mapped[list['Students']] = relationship('Students', back_populates='school')
    teachers: Mapped[list['Teachers']] = relationship('Teachers', back_populates='school')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='school')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='school')
    student_parents: Mapped[list['StudentParents']] = relationship('StudentParents', back_populates='school')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='school')
    payments: Mapped[list['Payments']] = relationship('Payments', back_populates='school')
    attendance: Mapped[list['Attendance']] = relationship('Attendance', back_populates='school')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='school')
