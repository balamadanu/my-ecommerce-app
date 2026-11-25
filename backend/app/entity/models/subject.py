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


class Subjects(Base):
    __tablename__ = 'subjects'
    __table_args__ = (
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='subjects_school_id_fkey'),
        PrimaryKeyConstraint('id', name='subjects_pkey'),
        UniqueConstraint('school_id', 'id', name='subjects_school_id_id_key'),
        UniqueConstraint('school_id', 'subject_code', name='subjects_school_id_subject_code_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    subject_code: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    school: Mapped['Schools'] = relationship('Schools', back_populates='subjects')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='subjects')
