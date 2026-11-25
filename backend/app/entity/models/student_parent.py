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


class StudentParents(Base):
    __tablename__ = 'student_parents'
    __table_args__ = (
        ForeignKeyConstraint(['school_id', 'parent_id'], ['parents.school_id', 'parents.id'], name='student_parents_school_id_parent_id_fkey'),
        ForeignKeyConstraint(['school_id', 'student_id'], ['students.school_id', 'students.id'], name='student_parents_school_id_student_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='student_parents_school_id_fkey'),
        PrimaryKeyConstraint('school_id', 'student_id', 'parent_id', name='student_parents_pkey')
    )

    school_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    student_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    parent_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    relationship_type: Mapped[Optional[str]] = mapped_column(String(30))
    is_primary: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))

    parents: Mapped['Parents'] = relationship('Parents', back_populates='student_parents')
    students: Mapped['Students'] = relationship('Students', back_populates='student_parents')
    school: Mapped['Schools'] = relationship('Schools', back_populates='student_parents')
