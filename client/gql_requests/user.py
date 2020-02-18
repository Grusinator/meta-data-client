get_user = """
{
  user {
    username
    firstName
    lastName
    email
  }
}
"""

get_dummy_user = """
    {
        dummy {
            firstName
            lastName
        }
    }
"""

authorize = """
    mutation LoginMutation($username: String!, $password: String!) {
        tokenAuth(username: $username, password: $password) {
            token
        }
    }
"""
