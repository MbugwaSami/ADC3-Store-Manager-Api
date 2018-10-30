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

        # test create user
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

    def test_user_data_is_not_empty(self):

        """This method tests wheather  user data is supplied.
           :param1:client.
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps({}),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Fields cannot be empty")
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user5),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Some fields are empty!")
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
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
        '/api/v2/users',
        headers=dict(Authorization="Bearer " + self.owner_token),
        data = json.dumps(self.test_user1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account alrleady exists")
        self.assertEqual(response.status_code, 200)

    def test_email_is_valid(self):
        """This method tests wheather user email is valaid.
           :param1:client
           :param2:user data
           :returns:response.
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user2),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Please enter a valaid email")
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
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"password should be between 6 and 12 characters, have atleast one lower_case,"
        +"one Upper_case,one number and one special character")
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
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Roles can only be admin or attendant")
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
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

        response = self.client.get(
        '/api/v2/users',
        headers=dict(Authorization="Bearer " + self.owner_token))
        self.assertEqual(response.status_code, 200)



    def test_login(self):
        """This method test wheather user can login.
           :param1:client.
           :param2:user data.
           :returns:response.

        """

        #test empty login
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps({}),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"please enter data to login")
        self.assertEqual(response.status_code, 200)

        #test valid login
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.test_login),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"wellcome SAMMY NJAU, you are loged in as attendant")
        self.assertEqual(response.status_code, 200)


        #test invalid login
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.test_login1),
        content_type = 'application/json'
        )


        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"wrong email or password")
        self.assertEqual(response.status_code, 200)

        
