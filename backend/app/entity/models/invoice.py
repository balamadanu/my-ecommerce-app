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


class Invoices(Base):
    __tablename__ = 'invoices'
    __table_args__ = (
        CheckConstraint('due_date IS NULL OR due_date >= invoice_date', name='invoices_check'),
        CheckConstraint("status::text = ANY (ARRAY['pending'::character varying, 'partially_paid'::character varying, 'paid'::character varying, 'overdue'::character varying, 'cancelled'::character varying]::text[])", name='invoices_status_check'),
        CheckConstraint('total_amount >= 0::numeric', name='invoices_total_amount_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='invoices_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'fee_structure_id'], ['fee_structures.school_id', 'fee_structures.id'], name='invoices_school_id_fee_structure_id_fkey'),
        ForeignKeyConstraint(['school_id', 'student_id'], ['students.school_id', 'students.id'], name='invoices_school_id_student_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='invoices_school_id_fkey'),
        PrimaryKeyConstraint('id', name='invoices_pkey'),
        UniqueConstraint('school_id', 'id', name='invoices_school_id_id_key'),
        UniqueConstraint('school_id', 'invoice_number', name='invoices_school_id_invoice_number_key'),
        Index('idx_invoices_status', 'school_id', 'status'),
        Index('idx_invoices_student', 'school_id', 'student_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    student_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    fee_structure_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    invoice_number: Mapped[str] = mapped_column(String(50), nullable=False)
    total_amount: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    invoice_date: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text('CURRENT_DATE'))
    due_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    status: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'pending'::character varying"))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='invoices')
    fee_structures: Mapped['FeeStructures'] = relationship('FeeStructures', back_populates='invoices')
    students: Mapped['Students'] = relationship('Students', back_populates='invoices')
    school: Mapped['Schools'] = relationship('Schools', back_populates='invoices')
    payments: Mapped[list['Payments']] = relationship('Payments', back_populates='invoices')
