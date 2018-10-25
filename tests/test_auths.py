import json

from tests import TestBase

# class for testing test_user
class TestAuths(TestBase):
    """This class has methods that test methods used in manipulation of user data"""

    def test_create_account(self):

        """This method tests wheather a user account has been created
           param1:client
           param2:response
        """

        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Email already registered",response_data["message"])

        # test user is unique
        response = self.client.post(
        '/api/v1/users',
        data = json.dumps(self.test_user),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Email already registered",response_data["message"])