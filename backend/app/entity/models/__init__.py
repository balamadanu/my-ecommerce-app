from app.entity.models.school import Schools
from app.entity.models.academic_year import AcademicYears
from app.entity.models.class_model import Classes
from app.entity.models.subject import Subjects
from app.entity.models.user import Users
from app.entity.models.exam import Exams
from app.entity.models.fee_structure import FeeStructures
from app.entity.models.parent import Parents
from app.entity.models.student import Students
from app.entity.models.teacher import Teachers
from app.entity.models.invoice import Invoices
from app.entity.models.section import Sections
from app.entity.models.student_parent import StudentParents
from app.entity.models.enrollment import Enrollments
from app.entity.models.payment import Payments
from app.entity.models.attendance import Attendance
from app.entity.models.exam_result import ExamResults

__all__ = [
    'Schools', 'AcademicYears', 'Classes', 'Subjects', 'Users',
    'Exams', 'FeeStructures', 'Parents', 'Students', 'Teachers',
    'Invoices', 'Sections', 'StudentParents', 'Enrollments',
    'Payments', 'Attendance', 'ExamResults',
]
