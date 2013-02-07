import simplejson
import urllib
import cgi
import urllib2
import urllib
import httplib
import oauth2 as oauth
from datetime import datetime
from urlparse import parse_qsl

from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.sites.models import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url, base36_to_int
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth.tokens import default_token_generator

from cross_founding_platform import settings
from cross_founding_platform.cross_founding.forms import PasswordRecoveryForm, EmailRecoveryForm, BackerRegistrationForm

FACEBOOK_OAUTH_DIALOG_URL = "https://www.facebook.com/dialog/oauth?"
FACEBOOK_ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token?'
FACEBOOK_GRAPH_API_URL = 'https://graph.facebook.com/me?access_token='
FACEBOOK_REDIRECT_URI = 'http://127.0.0.1:8000/facebook_register/'
FACEBOOK_APP_ID = settings.FACEBOOK_APP_ID
FACEBOOK_APP_SECRET = settings.FACEBOOK_SECRET

TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL  = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
TWITTER_AUTHENTICATE_URL = 'https://api.twitter.com/oauth/authenticate'
TWITTER_OAUTH_CONSUMER_KEY = "SiAxtvUQc6Z6bVR2Vi0A"
TWITTER_OAUTH_CONSUMER_SECRET_KEY = 'sQgtyyO7siQyqEx6609ZfC052lOzsmGSOOh9VG0yvuk'

def profile(request):
    return render_to_response("profile.html")


@sensitive_post_parameters()
@never_cache
@csrf_protect
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)

        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = settings.LOGIN_REDIRECT_URL

            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb36=None, token=None,
                           template_name='registration/password_reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=PasswordRecoveryForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):

    assert uidb36 is not None and token is not None

    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_complete')
    try:
        uid_int = base36_to_int(uidb36)
        user = User.objects.get(id=uid_int)

    except (ValueError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True

        if request.method == 'POST':
            form = set_password_form(user, request.POST)

            if form.is_valid():
                form.save()

                return HttpResponseRedirect(post_reset_redirect)

        else:
            form = set_password_form(None)

    else:
        validlink = False
        form = None
    context = {
        'form': form,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context, current_app=current_app)

@csrf_protect
def password_reset(request, is_admin_site=False,
                   template_name='registration/password_reset_form.html',
                   email_template_name='registration/password_reset_email.html',
                   subject_template_name='registration/password_reset_subject.txt',
                   password_reset_form=EmailRecoveryForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=None,
                   from_email=None,
                   current_app=None,
                   extra_context=None):
    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_done')
    if request.method == "POST":
        form = EmailRecoveryForm(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'token_generator': token_generator,
                'from_email': from_email,
                'email_template_name': email_template_name,
                'subject_template_name': subject_template_name,
                'request': request,
                }
            if is_admin_site:
                opts = dict(opts, domain_override=request.get_host())
            form.save(**opts)
            return HttpResponseRedirect(post_reset_redirect)
    else:
        form = password_reset_form()
    context = {
        'form': form,
        }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)

def facebook_register(request):
    if not 'code' in request.GET:
        key_value_perm_state = {'client_id': FACEBOOK_APP_ID, 'redirect_uri': FACEBOOK_REDIRECT_URI}

        return redirect(FACEBOOK_OAUTH_DIALOG_URL + urllib.urlencode(key_value_perm_state))

    else:
        code = request.GET['code']
        get_token = {'client_id': FACEBOOK_APP_ID, 'redirect_uri': FACEBOOK_REDIRECT_URI, 'client_secret': FACEBOOK_APP_SECRET, 'code': code}

        response = cgi.parse_qs(urllib.urlopen(FACEBOOK_ACCESS_TOKEN_URL + urllib.urlencode(get_token)).read())

        access_token = response['access_token'][0]
        get_data_url = FACEBOOK_GRAPH_API_URL + access_token

        json_data = urllib.urlopen(get_data_url).read()
        facebook_data = simplejson.loads(json_data)

        facebook_data['gender'] = 2 if facebook_data['gender'] == 'male' else 3

        birthday = str(datetime.date(datetime.strptime(facebook_data['birthday'], "%m/%d/%Y"))).split('-')

        facebook_data.update({'year_dob': birthday[0]})
        facebook_data.update({'month_dob': birthday[1]})
        facebook_data.update({'day_dob': birthday[2]})

        form = BackerRegistrationForm(facebook_data)

        return render(request, 'registration/registration_form.html', {'form': form})

def twitter_register(request):
    if not 'oauth_verifier' in request.GET:
        oauth_consumer = oauth.Consumer(key=TWITTER_OAUTH_CONSUMER_KEY, secret=TWITTER_OAUTH_CONSUMER_SECRET_KEY)
        oauth_client = oauth.Client(oauth_consumer)

        resp, content = oauth_client.request(TWITTER_REQUEST_TOKEN_URL, 'POST')
        content = dict(parse_qsl(content))

        return HttpResponseRedirect(TWITTER_AUTHENTICATE_URL + '?oauth_token=' + content['oauth_token'])

    else:
        oauth_consumer = oauth.Consumer(key=TWITTER_OAUTH_CONSUMER_KEY, secret=TWITTER_OAUTH_CONSUMER_SECRET_KEY)
        token = oauth.Token(request.GET['oauth_token'], TWITTER_OAUTH_CONSUMER_SECRET_KEY)
        token.set_verifier(request.GET['oauth_verifier'])

        oauth_client = oauth.Client(oauth_consumer, token)
        resp, content = oauth_client.request(TWITTER_ACCESS_TOKEN_URL, method='POST',
            body='oauth_verifier=%s' % request.GET['oauth_verifier'])

        access_token = dict(parse_qsl(content))

        json_data_url = 'https://api.twitter.com/1/users/show.json?screen_name=' + access_token[
                                                                                   'screen_name'] + '&amp;include_entities=true'
        json_data = urllib.urlopen(json_data_url).read()

        data = simplejson.loads(json_data)
        twitter_full_name = data['name'].split(' ')

        twitter_last_name = twitter_full_name[-1] if len(twitter_full_name) > 1 else ''

        twitter_data = {'username': data['screen_name'], 'first_name': twitter_full_name[0], 'last_name': twitter_last_name}

        form = BackerRegistrationForm(twitter_data)

        return render(request, 'registration/registration_form.html', {'form': form})