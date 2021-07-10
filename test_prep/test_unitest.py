# import unittest,json
# from app import app
# from unittest.mock import patch


# class FlaskTestCase(unittest.TestCase):

#     def test_index(self):
#         tester=app.test_client(self)
#         response = tester.get('/')
#         # print('response--->',response)
#         # print('response.data --->',response.data)
#         self.assertEqual(response.status_code,200)
#         self.assertDictEqual(response.get_json(),{'xyz':"Home page"})

#     def test_a(self):
#         tester=app.test_client(self)
#         response = tester.get('/a')
#         # print('response--->',response)
#         # print('response.data --->',response.data)
#         self.assertEqual(response.status_code,200)

# class FlaskTest_b_Case(unittest.TestCase):

#     def test_b(self):
#         tester=app.test_client(self)
#         payload={'name':'nisarg'}
#         response = tester.post('/c',json=payload, headers={'Content-Type': 'application/json'})
#         print(response)
#         print(response.get_json())
#         self.assertEqual(response.status_code,200)
#         self.assertDictEqual(response.get_json(),payload)

# if __name__ == '__main__':
#     unittest.main()
