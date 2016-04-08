from django.test import TestCase
from django.test.client import RequestFactory
from .views import create_user
from django.http import HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware

request_url = '/accounts/create_user/'

class CreateUserViewTestCase(TestCase):
  def makeRequest(self, body):
    request = self.request_factory.post(request_url, body)
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    return request

  def setUp(self):
    self.request_factory = RequestFactory()

  def testOnlyPostAccepted(self):
    """ This REST method only accepts POST requests. """
    request_body =  {}
    request = self.makeRequest(request_body)
    disallowed_methods = ["GET", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE", "CONNECT", "ASDF"]
    for method in disallowed_methods:
      request.method = method
      self.assertEqual(403, create_user(request).status_code)

  def testDuplicateUserError(self):
    """ Errors arising from creating a duplicate user are handled """
    request_body =  {
      "username":"test_duplicates",
      "email":"test",
      "password":"test",
      "address1":"",
      "address2":"",
      "city":"",
      "state":"",
      "zip_code":""
    }
    create_user(self.makeRequest(request_body))
    self.assertEqual(409, create_user(self.makeRequest(request_body)).status_code)

  def testProfileCreated(self):
    """ A profile for the user is created. """
    pass

  def testUserLoggedIn(self):
    """ After the user and profile are created, the user is logged in """
    pass

  def testAuthenticateFailureHandled(self):
    """ Errors from trying to authenticate the user are handled. """
    pass

  def testLoginFailureHandled(self):
    """ Errors from trying to log the user in are handled. """
    pass

  def test201OnSuccess(self):
    """ If a user is successfully created, it returns a 201. """
    pass
