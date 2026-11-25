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


class Classes(Base):
    __tablename__ = 'classes'
    __table_args__ = (
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='classes_school_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_pkey'),
        UniqueConstraint('school_id', 'id', name='classes_school_id_id_key'),
        UniqueConstraint('school_id', 'name', name='classes_school_id_name_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    grade_level: Mapped[Optional[int]] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    school: Mapped['Schools'] = relationship('Schools', back_populates='classes')
    exams: Mapped[list['Exams']] = relationship('Exams', back_populates='classes')
    fee_structures: Mapped[list['FeeStructures']] = relationship('FeeStructures', back_populates='classes')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='classes')
