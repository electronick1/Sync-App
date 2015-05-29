from django.shortcuts import render, redirect

from powerapp.core.models.oauth import AccessToken
from powerapp.core.models.integration import Integration
from powerapp.core.models.service import Service
from powerapp.core.oauth import get_client_by_name


def add_integration(request):
    """
    Add integration to user if user authenticate in google,
    else redirect to authentication url
    """
    user = request.user
    if is_authorized(user):
        integration_exists = Integration.objects.filter(service_id='powerapp_github_sync', user=user).exists()
        if not integration_exists:
            integration = Integration(service_id='powerapp_github_sync',
                                      user=user,
                                      settings={'from_todoist': True,
                                                'from_google': False})
            integration.save()

    return redirect('web_index')



def delete_integration(request, integration_id):
    user = request.user
    Integration.objects.get(user=user,
                            id=integration_id)\
                       .delete()
    return redirect('web_index')


def edit_integration(request, integration_id):
    integration = Integration.objects.get(id=integration_id)
    return render(request, get_template('edit'), {'integration': integration})


def get_template(name):
    return "powerapp_github_sync/%s.html" % name


def is_authorized(user):
    return AccessToken.objects.filter(user=user, client='github_sync').exists()
