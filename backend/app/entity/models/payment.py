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


class Payments(Base):
    __tablename__ = 'payments'
    __table_args__ = (
        CheckConstraint('amount > 0::numeric', name='payments_amount_check'),
        CheckConstraint("payment_method IS NULL OR (payment_method::text = ANY (ARRAY['cash'::character varying, 'card'::character varying, 'upi'::character varying, 'bank_transfer'::character varying, 'cheque'::character varying, 'online'::character varying]::text[]))", name='payments_payment_method_check'),
        CheckConstraint("status::text = ANY (ARRAY['pending'::character varying, 'completed'::character varying, 'failed'::character varying, 'refunded'::character varying]::text[])", name='payments_status_check'),
        ForeignKeyConstraint(['school_id', 'invoice_id'], ['invoices.school_id', 'invoices.id'], name='payments_school_id_invoice_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='payments_school_id_fkey'),
        PrimaryKeyConstraint('id', name='payments_pkey'),
        Index('idx_payments_invoice', 'school_id', 'invoice_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    invoice_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    amount: Mapped[decimal.Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    payment_date: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    payment_method: Mapped[Optional[str]] = mapped_column(String(30))
    transaction_reference: Mapped[Optional[str]] = mapped_column(String(150))
    status: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'completed'::character varying"))
    remarks: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    invoices: Mapped['Invoices'] = relationship('Invoices', back_populates='payments')
    school: Mapped['Schools'] = relationship('Schools', back_populates='payments')
