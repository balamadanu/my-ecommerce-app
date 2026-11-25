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


class FeeStructures(Base):
    __tablename__ = 'fee_structures'
    __table_args__ = (
        CheckConstraint('amount >= 0::numeric', name='fee_structures_amount_check'),
        CheckConstraint("frequency::text = ANY (ARRAY['monthly'::character varying, 'quarterly'::character varying, 'half_yearly'::character varying, 'annual'::character varying, 'one_time'::character varying]::text[])", name='fee_structures_frequency_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='fee_structures_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_id'], ['classes.school_id', 'classes.id'], name='fee_structures_school_id_class_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='fee_structures_school_id_fkey'),
        PrimaryKeyConstraint('id', name='fee_structures_pkey'),
        UniqueConstraint('school_id', 'id', name='fee_structures_school_id_id_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    fee_name: Mapped[str] = mapped_column(String(150), nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    frequency: Mapped[Optional[str]] = mapped_column(String(30), server_default=text("'annual'::character varying"))
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='fee_structures')
    classes: Mapped['Classes'] = relationship('Classes', back_populates='fee_structures')
    school: Mapped['Schools'] = relationship('Schools', back_populates='fee_structures')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='fee_structures')
