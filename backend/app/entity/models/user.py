from typing import Optional
import datetime
import decimal

from sqlalchemy import (
    BigInteger, Boolean, CheckConstraint, Date, DateTime,
    ForeignKeyConstraint, Identity, Index, Integer, Numeric,
    PrimaryKeyConstraint, String, Text, UniqueConstraint, func, text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.entity.models.school import Schools
    from app.entity.models.parent import Parents
    from app.entity.models.student import Students
    from app.entity.models.teacher import Teachers
    from app.entity.models.attendance import Attendance

class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint("role::text = ANY (ARRAY['admin'::character varying, 'teacher'::character varying, 'student'::character varying, 'parent'::character varying]::text[])", name='users_role_check'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='users_school_id_fkey'),
        PrimaryKeyConstraint('id', name='users_pkey'),
        UniqueConstraint('school_id', 'id', name='users_school_id_id_key'),
        Index('uq_users_school_email', 'school_id', func.lower('email'), unique=True)
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    full_name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    last_login: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    school: Mapped['Schools'] = relationship('Schools', back_populates='users')
    parents: Mapped[Optional['Parents']] = relationship('Parents', uselist=False, back_populates='users')
    students: Mapped[Optional['Students']] = relationship('Students', uselist=False, back_populates='users')
    teachers: Mapped[Optional['Teachers']] = relationship('Teachers', uselist=False, back_populates='users')
    attendance: Mapped[list['Attendance']] = relationship('Attendance', back_populates='users')
