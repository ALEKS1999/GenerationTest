import unittest
from datetime import date
from main import *
from institute import Institute

class TestGeneration(unittest.TestCase):
    
    def test_student_class(self):
        st = Student(172580, 'Кычкин Алексей')
        self.assertEqual('Кычкин Алексей', st.fio)
        self.assertEqual(172580, st.code)
        
    def test_group_class(self):
        spec = Specialization("ФИИТ")
        grp = Group("М-ФИИТ-21", 2021, spec)
        self.assertEqual('М-ФИИТ-21', grp.name)
        self.assertEqual(2021, grp.year)
        self.assertEqual("ФИИТ", grp.specialization.name)
        
    def test_exam_class(self):
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', "Эверстов Владимир Васильевич")
        self.assertEqual('Основы программирования', exam.subject.name)
        self.assertEqual(date(2021,2,12), exam.examDate)
        self.assertEqual("2021", exam.year)
        self.assertEqual("Эверстов Владимир Васильевич", exam.lecturer_fio)
        
    def test_exampoints_class(self):
        st = Student(172580, 'Кычкин Алексей')
        examPo = ExamPoints(st, 55.5, 30.0)
        self.assertEqual('Кычкин Алексей', examPo.student.fio)
        self.assertEqual(55.5, examPo.inPoints)
        self.assertEqual(30.0, examPo.examPoints)
        
    def test_subject_class(self):
        spec = Specialization("ФИИТ")
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        self.assertEqual('Б1', subj.code)
        self.assertEqual('Основы программирования', subj.name)
        self.assertEqual(1, subj.semester)
        self.assertEqual(172, subj.hours)
        self.assertEqual("ФИИТ", subj.specialization.name)
        
    def test_specialization_class(self):
        spec = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", spec.name)
        

if __name__ == 'main':
    unittest.main()