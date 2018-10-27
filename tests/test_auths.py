import json

from tests import TestBase

# class for testing test_user
class TestAuths(TestBase):
    """This class has methods that test methods used in manipulation of user data."""

    def test_create_account(self):

        """This method tests wheather a user account has been created.
           :param1:client.
           :user data
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("User account succesfuly created",response_data["message"])
        self.assertEqual(response.status_code, 201)

    def test_user_data_is_not_empty(self):

        """This method tests wheather  user data is supplied.
           :param1:client.
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps({}),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Fields cannot be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user5),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Some fields are empty!",response_data["message"])
        self.assertEqual(response.status_code, 200)



    def test_user_exists(self):
        """This method tests wheather a user account alrleady exists.
           :param1:client.
           :param2:user data.
           :returns:response:
        """


        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("User account succesfuly created",response_data["message"])
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("User account alrleady exists",response_data["message"])
        self.assertEqual(response.status_code, 200)

    def test_email_is_valid(self):
        """This method tests wheather user email is valaid.
           :param1:client.
           :param2:user data
           :returns:response.
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user2),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Please enter a valaid email",response_data["message"])
        self.assertEqual(response.status_code, 200)

    def test_password_strength(self):
        """This method checks wheather password meets strength criteria
           :param1:client.
           :param2:user data.
           returns:response.
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user3),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("password should be between 6 and 12 characters, have atleast one lower_case,"
        +"one Upper_case,one number and one special character",response_data["message"])
        self.assertEqual(response.status_code, 200)

    def test_role_is_valid(self):
        """This method test wheather user role is checkedself.
           :param1:client.
           :param2:user data.
           :returns:response.

        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user4),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Roles can only be admin or attendant",response_data["message"])
        self.assertEqual(response.status_code, 200)

    def test_get_users(self):
        """This method tests for methods for getting users.
           :param1:client.
           :param2:user data.
           :returns:response.
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user6),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("User account succesfuly created",response_data["message"])
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v2/users')
        self.assertEqual(response.status_code, 200)
