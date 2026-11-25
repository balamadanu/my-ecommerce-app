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


class Parents(Base):
    __tablename__ = 'parents'
    __table_args__ = (
        ForeignKeyConstraint(['school_id', 'user_id'], ['users.school_id', 'users.id'], name='parents_school_id_user_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='parents_school_id_fkey'),
        PrimaryKeyConstraint('id', name='parents_pkey'),
        UniqueConstraint('school_id', 'id', name='parents_school_id_id_key'),
        UniqueConstraint('school_id', 'user_id', name='parents_school_id_user_id_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    occupation: Mapped[Optional[str]] = mapped_column(String(150))
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    address: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='parents')
    school: Mapped['Schools'] = relationship('Schools', back_populates='parents')
    student_parents: Mapped[list['StudentParents']] = relationship('StudentParents', back_populates='parents')
