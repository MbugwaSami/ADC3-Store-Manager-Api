import json

from .base_test import TestBase

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


         # test empty user data
    def test_empty_data(self):

        """This method tests for empty user data.
           :param1:client.
           :products data
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

        # test data with some empty field
    def test_data_with_empty_fields(self):

        """This method tests for empty user data fields.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user5),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Some fields are empty!")
        self.assertEqual(response.status_code, 200)


        # test user exist
    def test_user_already_exists(self):

        """This method tests for an existing user.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user1),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response = self.client.post(
        '/api/v2/users',
        headers=dict(Authorization="Bearer " + self.owner_token),
        data = json.dumps(self.test_user1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account alrleady exists")
        self.assertEqual(response.status_code, 200)

       # test email is valid
    def test_invalid_email(self):

        """This method tests for an invalid email.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user2),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"Please enter a valid email")
        self.assertEqual(response.status_code, 200)


        # test password is strong
    def test_weak_password(self):

        """This method tests for a weak password.
           :param1:client.
           :products data
           :returns:response:
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

        # test role is valid
    def test_invalid_role(self):

        """This method tests for an invalid role.
           :param1:client.
           :products data
           :returns:response:
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


    def test_empty_login(self):
        """This method test whether user cannot login with empty data.
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
    def test_login(self):

        """This method tests a valid login.
           :param1:client.
           :products data
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.login_user),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.test_login),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"wellcome SAMMY MBUGUA, you are loged in as attendant")
        self.assertEqual(response.status_code, 201)



        #test invalid login
    def test_invalid_login(self):

        """This method tests for a valid login.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.test_login1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"wrong email or password")
        self.assertEqual(response.status_code, 401)

    def test_logout(self):

        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user7),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(dict(
        email = "sammy@gmail.com",
        password = "Mwoboko10@"
        )),
        content_type = 'application/json'
        )

        attendant_token = json.loads(response.data.decode())['token']

        response = self.client.post(
        '/api/v2/users/logout',
        headers=dict(Authorization="Bearer " + attendant_token),
        content_type = 'application/json'

        )
        response_data = json.loads(response.data)

        self.assertEqual(response_data["message"],"You have been logged out")
        self.assertEqual(response.status_code, 201)


        # test create user by attendant
    def test_atendant_create_account(self):

        """This method tests an attendant cannot create an account.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user7),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)

    def test_attendant_view_all_users(self):

        """This method tests attendant cannot view all users.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/users',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)

    def test_admin_view_all_users(self):

        """This method tests admin can view all users.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/users',
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"This are users in the system")
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
         """This method tests the method for updating user details
            :param1:client.
            :products data
            :returns:response:
         """
         response = self.client.put(
         '/api/v2/users/1',
         data = json.dumps(self.test_user8),
         headers=dict(Authorization="Bearer " + self.owner_token),
         content_type = 'application/json'
         )

         response_data = json.loads(response.data)
         self.assertEqual(response_data["message"],"Updated succesfuly")
         self.assertEqual(response.status_code, 200)

    def test_update_user_not_existing(self):

         """This method tests the method for updating user details of user not in the system
            :param1:client.
            :products data
            :returns:response:
         """

         response = self.client.put(
         '/api/v2/users/8888',
         headers=dict(Authorization="Bearer " + self.owner_token),
         data = json.dumps(self.test_product),
         content_type = 'application/json'
         )

         response_data = json.loads(response.data)
         self.assertEqual("This user is not in the system",response_data["message"])
         self.assertEqual(response.status_code, 200)



    def test_delete_user(self):
        """This method tests the method for deleting a user.
           :param1:client.
           :products data
           :returns:response:
        """

        response = self.client.delete(
        '/api/v2/users/3',
        headers=dict(Authorization="Bearer " + self.owner_token)
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], "one user deleted")
        self.assertEqual(response.status_code, 200)
