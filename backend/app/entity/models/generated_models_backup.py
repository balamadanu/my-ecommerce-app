from typing import Optional
import datetime
import decimal

from sqlalchemy import BigInteger, Boolean, CheckConstraint, Date, DateTime, ForeignKeyConstraint, Identity, Index, Integer, Numeric, PrimaryKeyConstraint, String, Text, UniqueConstraint, func, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.database.base import Base


class Schools(Base):
    __tablename__ = 'schools'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='schools_pkey'),
        UniqueConstraint('code', name='schools_code_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    code: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(Text)
    phone: Mapped[Optional[str]] = mapped_column(String(20))
    email: Mapped[Optional[str]] = mapped_column(String(150))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    updated_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped[list['AcademicYears']] = relationship('AcademicYears', back_populates='school')
    classes: Mapped[list['Classes']] = relationship('Classes', back_populates='school')
    subjects: Mapped[list['Subjects']] = relationship('Subjects', back_populates='school')
    users: Mapped[list['Users']] = relationship('Users', back_populates='school')
    exams: Mapped[list['Exams']] = relationship('Exams', back_populates='school')
    fee_structures: Mapped[list['FeeStructures']] = relationship('FeeStructures', back_populates='school')
    parents: Mapped[list['Parents']] = relationship('Parents', back_populates='school')
    students: Mapped[list['Students']] = relationship('Students', back_populates='school')
    teachers: Mapped[list['Teachers']] = relationship('Teachers', back_populates='school')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='school')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='school')
    student_parents: Mapped[list['StudentParents']] = relationship('StudentParents', back_populates='school')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='school')
    payments: Mapped[list['Payments']] = relationship('Payments', back_populates='school')
    attendance: Mapped[list['Attendance']] = relationship('Attendance', back_populates='school')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='school')


class AcademicYears(Base):
    __tablename__ = 'academic_years'
    __table_args__ = (
        CheckConstraint('end_date > start_date', name='academic_years_check'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='academic_years_school_id_fkey'),
        PrimaryKeyConstraint('id', name='academic_years_pkey'),
        UniqueConstraint('school_id', 'id', name='academic_years_school_id_id_key'),
        UniqueConstraint('school_id', 'name', name='academic_years_school_id_name_key'),
        Index('uq_current_academic_year', 'school_id', postgresql_where='(is_current = true)', unique=True)
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_current: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('false'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    school: Mapped['Schools'] = relationship('Schools', back_populates='academic_years')
    exams: Mapped[list['Exams']] = relationship('Exams', back_populates='academic_years')
    fee_structures: Mapped[list['FeeStructures']] = relationship('FeeStructures', back_populates='academic_years')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='academic_years')
    sections: Mapped[list['Sections']] = relationship('Sections', back_populates='academic_years')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='academic_years')


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


class Exams(Base):
    __tablename__ = 'exams'
    __table_args__ = (
        CheckConstraint('start_date IS NULL OR end_date IS NULL OR end_date >= start_date', name='exams_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='exams_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_id'], ['classes.school_id', 'classes.id'], name='exams_school_id_class_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='exams_school_id_fkey'),
        PrimaryKeyConstraint('id', name='exams_pkey'),
        UniqueConstraint('school_id', 'id', name='exams_school_id_id_key'),
        Index('idx_exams_academic_year', 'school_id', 'academic_year_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    exam_type: Mapped[Optional[str]] = mapped_column(String(50))
    start_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    description: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='exams')
    classes: Mapped['Classes'] = relationship('Classes', back_populates='exams')
    school: Mapped['Schools'] = relationship('Schools', back_populates='exams')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='exams')


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


class Students(Base):
    __tablename__ = 'students'
    __table_args__ = (
        ForeignKeyConstraint(['school_id', 'user_id'], ['users.school_id', 'users.id'], name='students_school_id_user_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='students_school_id_fkey'),
        PrimaryKeyConstraint('id', name='students_pkey'),
        UniqueConstraint('school_id', 'admission_number', name='students_school_id_admission_number_key'),
        UniqueConstraint('school_id', 'id', name='students_school_id_id_key'),
        UniqueConstraint('school_id', 'user_id', name='students_school_id_user_id_key'),
        Index('idx_students_school', 'school_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    admission_number: Mapped[str] = mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    date_of_birth: Mapped[Optional[datetime.date]] = mapped_column(Date)
    gender: Mapped[Optional[str]] = mapped_column(String(20))
    blood_group: Mapped[Optional[str]] = mapped_column(String(10))
    address: Mapped[Optional[str]] = mapped_column(Text)
    admission_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    users: Mapped[Optional['Users']] = relationship('Users', back_populates='students')
    school: Mapped['Schools'] = relationship('Schools', back_populates='students')
    invoices: Mapped[list['Invoices']] = relationship('Invoices', back_populates='students')
    student_parents: Mapped[list['StudentParents']] = relationship('StudentParents', back_populates='students')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='students')


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


class Sections(Base):
    __tablename__ = 'sections'
    __table_args__ = (
        CheckConstraint('capacity IS NULL OR capacity > 0', name='sections_capacity_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='sections_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_id'], ['classes.school_id', 'classes.id'], name='sections_school_id_class_id_fkey'),
        ForeignKeyConstraint(['school_id', 'class_teacher_id'], ['teachers.school_id', 'teachers.id'], name='sections_school_id_class_teacher_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='sections_school_id_fkey'),
        PrimaryKeyConstraint('id', name='sections_pkey'),
        UniqueConstraint('school_id', 'class_id', 'academic_year_id', 'name', name='sections_school_id_class_id_academic_year_id_name_key'),
        UniqueConstraint('school_id', 'id', 'class_id', 'academic_year_id', name='sections_school_id_id_class_id_academic_year_id_key'),
        UniqueConstraint('school_id', 'id', name='sections_school_id_id_key')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    capacity: Mapped[Optional[int]] = mapped_column(Integer)
    class_teacher_id: Mapped[Optional[int]] = mapped_column(BigInteger)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='sections')
    classes: Mapped['Classes'] = relationship('Classes', back_populates='sections')
    teachers: Mapped[Optional['Teachers']] = relationship('Teachers', back_populates='sections')
    school: Mapped['Schools'] = relationship('Schools', back_populates='sections')
    enrollments: Mapped[list['Enrollments']] = relationship('Enrollments', back_populates='sections')


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


class Enrollments(Base):
    __tablename__ = 'enrollments'
    __table_args__ = (
        CheckConstraint("status::text = ANY (ARRAY['active'::character varying, 'completed'::character varying, 'transferred'::character varying, 'withdrawn'::character varying]::text[])", name='enrollments_status_check'),
        ForeignKeyConstraint(['school_id', 'academic_year_id'], ['academic_years.school_id', 'academic_years.id'], name='enrollments_school_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'section_id', 'class_id', 'academic_year_id'], ['sections.school_id', 'sections.id', 'sections.class_id', 'sections.academic_year_id'], name='enrollments_school_id_section_id_class_id_academic_year_id_fkey'),
        ForeignKeyConstraint(['school_id', 'student_id'], ['students.school_id', 'students.id'], name='enrollments_school_id_student_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='enrollments_school_id_fkey'),
        PrimaryKeyConstraint('id', name='enrollments_pkey'),
        UniqueConstraint('school_id', 'id', name='enrollments_school_id_id_key'),
        UniqueConstraint('school_id', 'section_id', 'roll_number', name='enrollments_school_id_section_id_roll_number_key'),
        UniqueConstraint('school_id', 'student_id', 'academic_year_id', name='enrollments_school_id_student_id_academic_year_id_key'),
        Index('idx_enrollments_class', 'school_id', 'class_id', 'section_id'),
        Index('idx_enrollments_student', 'school_id', 'student_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    student_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    academic_year_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    class_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    section_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    roll_number: Mapped[Optional[str]] = mapped_column(String(30))
    enrollment_date: Mapped[Optional[datetime.date]] = mapped_column(Date, server_default=text('CURRENT_DATE'))
    status: Mapped[Optional[str]] = mapped_column(String(20), server_default=text("'active'::character varying"))
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    academic_years: Mapped['AcademicYears'] = relationship('AcademicYears', back_populates='enrollments')
    sections: Mapped['Sections'] = relationship('Sections', back_populates='enrollments')
    students: Mapped['Students'] = relationship('Students', back_populates='enrollments')
    school: Mapped['Schools'] = relationship('Schools', back_populates='enrollments')
    attendance: Mapped[list['Attendance']] = relationship('Attendance', back_populates='enrollments')
    exam_results: Mapped[list['ExamResults']] = relationship('ExamResults', back_populates='enrollments')


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


class ExamResults(Base):
    __tablename__ = 'exam_results'
    __table_args__ = (
        CheckConstraint('marks_obtained <= maximum_marks', name='exam_results_check'),
        CheckConstraint('marks_obtained >= 0::numeric', name='exam_results_marks_obtained_check'),
        CheckConstraint('maximum_marks > 0::numeric', name='exam_results_maximum_marks_check'),
        ForeignKeyConstraint(['school_id', 'enrollment_id'], ['enrollments.school_id', 'enrollments.id'], name='exam_results_school_id_enrollment_id_fkey'),
        ForeignKeyConstraint(['school_id', 'exam_id'], ['exams.school_id', 'exams.id'], name='exam_results_school_id_exam_id_fkey'),
        ForeignKeyConstraint(['school_id', 'subject_id'], ['subjects.school_id', 'subjects.id'], name='exam_results_school_id_subject_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['schools.id'], name='exam_results_school_id_fkey'),
        PrimaryKeyConstraint('id', name='exam_results_pkey'),
        UniqueConstraint('school_id', 'exam_id', 'enrollment_id', 'subject_id', name='exam_results_school_id_exam_id_enrollment_id_subject_id_key'),
        Index('idx_exam_results_exam', 'school_id', 'exam_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True, autoincrement=True)
    school_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    exam_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    enrollment_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    subject_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    marks_obtained: Mapped[decimal.Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    maximum_marks: Mapped[decimal.Decimal] = mapped_column(Numeric(8, 2), nullable=False)
    grade: Mapped[Optional[str]] = mapped_column(String(10))
    remarks: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))

    enrollments: Mapped['Enrollments'] = relationship('Enrollments', back_populates='exam_results')
    exams: Mapped['Exams'] = relationship('Exams', back_populates='exam_results')
    subjects: Mapped['Subjects'] = relationship('Subjects', back_populates='exam_results')
    school: Mapped['Schools'] = relationship('Schools', back_populates='exam_results')
