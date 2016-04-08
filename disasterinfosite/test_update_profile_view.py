from django.test import TestCase
from django.test.client import RequestFactory
from .views import update_profile, create_user
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User

request_url = '/accounts/update_profile/'
class FakeUser():
  def is_authenticated(self):
    return False

class UpdateProfileViewTestCase(TestCase):
  def makeRequest(self, body):
    request = self.request_factory.post(request_url, body)
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    return request

  def setUp(self):
    self.request_factory = RequestFactory()
    user_body =  {
      "username":"created_user",
      "email":"created_user",
      "password":"test_created",
      "address1":"created address1",
      "address2":"created address2",
      "city":"created city",
      "state":"created state",
      "zip_code":"created zip"
    }
    create_user(self.makeRequest(user_body))
    self.created_user = User.objects.get(username="created_user")

  def testOnlyPostAccepted(self):
    """ This REST endpoint only accepts POST requests. """
    request_body =  {}
    request = self.makeRequest(request_body)
    disallowed_methods = ["GET", "HEAD", "PUT", "DELETE", "OPTIONS", "TRACE", "CONNECT", "ASDF"]
    for method in disallowed_methods:
      request.method = method
      self.assertEqual(403, update_profile(request).status_code)

  def testOnlyAuthenticatedUsers(self):
    """ Only authenticated users can update their profile. """
    request_body =  {}
    request = self.makeRequest(request_body)
    request.user = FakeUser()
    self.assertEqual(403, update_profile(request).status_code)

  def testProfileSaveFails(self):
    """ It returns a 500 when the profile fails to save """
    request_body = {
      "invalid_field": "foo"
    }
    request = self.makeRequest(request_body)
    request.user = self.created_user
    self.assertEqual(500, update_profile(request).status_code)

  def testProfileUpdated(self):
    """ The profile gets updated with the new data """

  def test201Success(self):
    """ It returns a 201 on success """

