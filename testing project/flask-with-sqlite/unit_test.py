import unittest
from app import app

class FlaskTest(unittest.TestCase):
    
    # Ensure that Flask app is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Ensure that the home page returns the correct content
    def test_home_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'Home Page' in response.data)

    # Ensure that adding a new student page returns the correct content
    def test_add_student_page_content(self):
        tester = app.test_client(self)
        response = tester.get('/addstudent')
        self.assertTrue(b'Add New Student' in response.data)

    # Ensure that adding a new student works correctly
    def test_add_student(self):
        tester = app.test_client(self)
        response = tester.post('/addrec', data=dict(name='John Doe', address='123 Main St', city='Anytown', pin='12345'), follow_redirects=True)
        self.assertIn(b'Record successfully added!', response.data)

    # Ensure that listing students page returns the correct content
    def test_list_students_page_content(self):
        tester = app.test_client(self)
        response = tester.get('/list')
        self.assertTrue(b'List of Students' in response.data)

if __name__ == '__main__':
    unittest.main()
