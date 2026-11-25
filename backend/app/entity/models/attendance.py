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


class Attendance(Base):
    __tablename__ = 'attendance'
    __table_args__ = (
        CheckConstraint("status::text = ANY (ARRAY['present'::character varying, 'absent'::character varying, 'late'::character varying, 'half_day'::character varying, 'leave'::character varying]::text[])", name='attendance_status_check'),
        ForeignKeyConstraint(['school_id', 'enrollment_id'], ['enrollments.school_id', 'enrollments.id'], name='attendance_school_id_enrollment_id_fkey'),
        ForeignKeyConstraint(['school_id', 'marked_by'], ['users.school_id', 'users.id'], name='attendance_school_id_marked_by_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='attendance_school_id_fkey'),
        PrimaryKeyConstraint('id', name='attendance_pkey'),
        UniqueConstraint('school_id', 'enrollment_id', 'attendance_date', name='attendance_school_id_enrollment_id_attendance_date_key'),
        UniqueConstraint('school_id', 'id', name='attendance_school_id_id_key'),
        Index('idx_attendance_date', 'school_id', 'attendance_date'),
        Index('idx_attendance_enrollment', 'school_id', 'enrollment_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    enrollment_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    attendance_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    remarks: Mapped[Optional[str]] = mapped_column(Text)
    marked_by: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    enrollments: Mapped['Enrollments'] = relationship('Enrollments', back_populates='attendance')
    users: Mapped[Optional['Users']] = relationship('Users', back_populates='attendance')
    school: Mapped['Schools'] = relationship('Schools', back_populates='attendance')
