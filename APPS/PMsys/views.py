import json, re
from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.views.generic.base import View

from utils.mixin_utils import LoginRequiredMixin

from rbac.models import Menu, Role
from system.models import SystemSetup
from PMsys import models as pms
from PMsys.forms import ItemForm

User = get_user_model()
# Create your views here.


class ProjectView(LoginRequiredMixin, View):

    def get(self, request):
        ret = SystemSetup.getSystemSetupLastData()
        return render(request, 'PMsys/pmsys_index.html', ret)


class ProjectOverView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)   # 检查路径是否授权
        ret.update(SystemSetup.getSystemSetupLastData())
        # fields = ['id', 'item', 'user', 'create_time', 'status']
        data = [{'name': '张三', 'x':'120.360389', 'y':'30.283525', 'status':'途中'},]

        ret['data'] = json.dumps(data)

        return render(request, 'PMsys/pro_overview/pro_overview.html', ret)


class ProjectListView(LoginRequiredMixin, View):

    def get(self, request):
        ret = Menu.getMenuByRequestUrl(url=request.path_info)  # 检查路径是否授权
        ret.update(SystemSetup.getSystemSetupLastData())
        fields = ['id', 'item_type', 'name', 'status', 'address', 'image']
        pms.Items.objects.filter(pk=7)
        if 'status' in request.session and request.session['status']:
            val = request.session['status'].split('_')[1]
            if not val:
                ret['data'] = pms.Items.objects.all().order_by('-id').distinct()
            else:
                ret['data'] = pms.Items.objects.filter(status=int(val)).order_by('-id').distinct()
        else:
            ret['data'] = pms.Items.objects.all()
        ret['itemfacilitys'] = pms.ItemFacilitys.objects.all()
        # pms.ItemFacilitys.objects.filter(itempower_items)
        print(ret['itemfacilitys'][0].facilitys.get_modal_display())
        print(ret['itemfacilitys'][0].itempower.items)
        return render(request, 'PMsys/pro_list/pro_list.html', ret)

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            item = get_object_or_404(pms.Items, pk=int(request.POST.get('id')))
            item.status = request.POST['status']
            item.save()
            ret = {}
        else:
            request.session['status'] = 'show_' + request.POST['show']
            ret = {}
        return HttpResponse(json.dumps(ret), content_type='application/json')


class ProjectNewView(LoginRequiredMixin, View):

    def get(self, request):
        manufacturers = pms.Manufacturer.objects.values()
        ret = {
            'manufacturers': manufacturers,
        }
        return render(request, 'PMsys/new_pro/new_pro.html', ret)

    def post(self, request):
        print(request.POST)
        item_form = ItemForm(request.POST)
        print(item_form)
        if item_form.is_valid():
            item_form.save()
            ret = {'status': 'success'}
            print('保存成功')
        else:
            print('保存失败')
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(item_form.errors)
            itemform_errors = re.findall(pattern, errors)
            ret = {
                'status': 'fail',
                'itemform_errors': itemform_errors[0]
            }

        return HttpResponse(json.dumps(ret), content_type='application/json')


class ProjectWorklogView(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'PMsys/work_log/work_log.html')

    def post(self, request):
        a = request.POST
        print(a.get('proName'))
        print(a['state'])
        ret = {
            'msg': 'abc'
        }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class ProjectFacilities(LoginRequiredMixin, View):

    def get(self, request):

        return render(request, 'PMsys/pro_facil/pro_facil.html')