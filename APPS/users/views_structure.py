import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from django.views.generic.base import View
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from APPS.users.models import Structure
from rbac.models import Menu
from system.models import SystemSetup

User = get_user_model()


class StructureView(LoginRequiredMixin, View):
    """
    组织架构管理
    """

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)
        ret.update(SystemSetup.getSystemSetupLastData())
        return render(request, 'system/structure')