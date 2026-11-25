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


class Teachers(Base):
    __tablename__ = 'teachers'
    __table_args__ = (
        ForeignKeyConstraint(['school_id', 'user_id'], ['users.school_id', 'users.id'], name='teachers_school_id_user_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='teachers_school_id_fkey'),
        PrimaryKeyConstraint('id', name='teachers_pkey'),
        UniqueConstraint('school_id', 'employee_number', name='teachers_school_id_employee_number_key'),
        UniqueConstraint('school_id', 'id', name='teachers_school_id_id_key'),
        UniqueConstraint('school_id', 'user_id', name='teachers_school_id_user_id_key'),
        Index('idx_teachers_school', 'school_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    employee_number: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    qualification: Mapped[Optional[str]] = mapped_column(String(200))
    joining_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    specialization: Mapped[Optional[str]] = mapped_column(String(150))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='teachers')
    school: Mapped['Schools'] = relationship('Schools', back_populates='teachers')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='teachers')
