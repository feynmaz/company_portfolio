from sre_constants import FAILURE
from .models import *
from users.models import *
import re


def detail_context_processor(request):
    
    context = {'allow_update': False }
    company_pk = get_company_pk(request)

    if company_pk and request.user.pk:
        if is_user_of_company(company_pk, request.user.pk):
            context['allow_update'] = True
            
    return context


def get_company_pk(request):
    match = re.match(r'/(?P<pk>\d+)/', str(request.path))
    if match:
        return int(match.group('pk'))
    return None


def is_user_of_company(company_pk, user_pk):
    if UserCompanyRelationship.objects.filter(
        company_id=company_pk, user_id=user_pk):
        return True
    else:
        return False