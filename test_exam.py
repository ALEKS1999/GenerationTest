import unittest
from institute import Institute
from main import Exam, Specialization, Subject
from datetime import date

class TestAddExam(unittest.TestCase):
    
    def test_1(self): # correct add(One object)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.add_exam(exam)
        self.assertEqual(len(inst.exams), 1)
    
    def test_2(self): # correct add(Two objects)
        spec1 = Specialization('ФИИТ')
        spec2 = Specialization("ИВТ")
        subj1 = Subject('Б1', 'Основы программирования', 1, 172, spec1)
        subj2 = Subject('Б1', 'Основы программирования', 1, 172, spec2)
        examDate = date(2021,2,12)
        exam1 = Exam(subj1, examDate, '2021', "Эверстов Владимир Васильевич")
        exam2 = Exam(subj2, examDate, '2021', "Эверстов Владимир Васильевич")
        inst = Institute()
        inst.add_exam(exam1)
        inst.add_exam(exam2)
        self.assertEqual(len(inst.exams), 2)    
        
    def test_3(self): # incorrect add(None object)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(None)
        self.assertEqual("Exam is null", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
    def test_4(self): # incorrect add(Existing object)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', "Эверстов Владимир Васильевич")
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(exam)
            inst.add_exam(exam)
        self.assertEqual("Exam already exist", str(context.exception))
        self.assertEqual(len(inst.exams), 1)
        
    def test_5(self): # incorrect add(Wrong type)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(1)
        self.assertEqual("Wrong type", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
    def test_6(self): # incorrect add(Wrong lecturer type)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', 12)
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(exam)
        self.assertEqual("Wrong lecturer type", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
    def test_7(self): # incorrect add(Lecturer fio is null)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '2021', '')
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(exam)
        self.assertEqual("Lecturer fio is null", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
    def test_8(self): # incorrect add(Wrong year type)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, 1, "Эверстов Владимир Васильевич")
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(exam)
        self.assertEqual("Wrong year type", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
    def test_9(self): # incorrect add(Year is null)
        spec = Specialization('ФИИТ')
        subj = Subject('Б1', 'Основы программирования', 1, 172, spec)
        examDate = date(2021,2,12)
        exam = Exam(subj, examDate, '', "Эверстов Владимир Васильевич")
        inst = Institute()
        with self.assertRaises(Exception) as context:
            inst.add_exam(exam)
        self.assertEqual("Year is null", str(context.exception))
        self.assertEqual(len(inst.exams), 0)
        
class TestGetExam(unittest.TestCase):
    
    def test_1(self):
        pass