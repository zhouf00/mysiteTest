import json, re, os
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from utils.tools.rendom_pwd import pwdlist

from rbac.models import Menu
from system.models import SystemSetup
from PMsys import models as pms
from PMsys.call_project import NewPower
from PMsys.forms import (ItemServerForm, DevinfoForm, ManuinfoForm, FacilityForm, SensorForm,
                         PowerForm, ImageForm, LinkForm)


class ListDevView(LoginRequiredMixin, View):
    """设备列表信息"""

    def get(self, request):
        if 'id' in request.GET and request.GET['id']:
            request.session['item_id'] = request.GET['id']
            request.session['item_name'] = pms.Items.objects.filter(pk=request.GET['id'])[0].name
            # print(pms.Items.objects.filter(pk=request.GET['id'])[0])
        data = pms.ItemPower.objects.filter(items=request.session['item_id']).order_by('p_title')
        if data:
            item_facilitys = pms.ItemFacilitys.objects.filter(itempower=data[0])
        else:
            item_facilitys = None
        # print(item_facilitys)
        dev = {'id1': '123'}
        ret = {
            'dev': json.dumps(dev),
            'data': data,
            'item_facilitys': item_facilitys
        }
        # print(ret['data'])
        return render(request, 'PMsys/pro_list/detail/dev_list.html', ret)

    def post(self, request):
        # for var in json.loads(request.POST['sensor']):
        #     print(var['b'])
        ret = {}

        return HttpResponse(json.dumps(ret), content_type='application/json')


class ListDevDetailView(LoginRequiredMixin, View):
    """设备查看视图"""

    def get(self, request):
        # 清空数据
        # item = pms.Items.objects.filter(pk=request.session['item_id'])[0]
        # item.powers.clear()
        # item.save()
        windpowers = pms.WindPower.objects.all()
        facilitys = pms.FacilityType.objects.all()
        sensors = pms.SensorType.objects.all()
        # print(request.GET)
        ret = {
            'windpowers': windpowers,
            'facilitys': facilitys,
            'sensors': sensors,
        }
        if 'powerId' in request.GET and request.GET['powerId']:
            item_power = pms.ItemPower.objects.filter(pk=int(request.GET['powerId']))[0]
            item_facility = pms.ItemFacilitys.objects.filter(itempower=item_power)
            item_sensors = pms.ItemSensors.objects.filter(itemfacility=item_facility[0])
            # print(item_facility[0], item_sensors)
            ret['item_power'] = item_power
            ret['item_facility'] = item_facility[0]
            ret['item_sensors'] = item_sensors
            # print('有ID')
        else:
            pass
            # print('无ID')
        return render(request, 'PMsys/pro_list/detail/dev_detail.html', ret)

    def post(self, request):
        try:
            if 'powerId' in request.POST and request.POST['powerId']:
                print('已经存在')
                newpower = NewPower(request)
                newpower.power_upline() # 保存风机
                # newpower.power_del() # 删除风机
                ret = {
                    'result': 'sussecc'
                }

            else:
                print('不存在')
                newpower = NewPower(request, 0)
                newpower.power_upline()
                ret = {
                    'result': 'sussecc',
                }
        except Exception as e:
            print(e)
            if 'status' in str(e):
                e = '风机状态不能为空'
            elif 'windpower_id' in str(e):
                e = '风机型号不能为空'
            ret = {
                'result': 'fail',
                'message': str(e)
            }
            return HttpResponse(json.dumps(ret), content_type='application/json')
        else:
            return HttpResponse(json.dumps(ret), content_type='application/json')


class ListServerView(LoginRequiredMixin, View):
    """服务器视图"""

    def get(self, request):
        request.session['status'] = None
        fields = ['id', 'server_type', 'server_model', 'sn', 'os_release', 'soft_release', 'cpu', 'cpu_count',
                  'ram', 'disk_type', 'disk_size', 'disk_count', 'raid_type', 'place', 'pc_username', 'pc_passwd',
                  'nic1', 'nic2', 'nic3', 'nic4', 'disk_unit', 'memo']
        if 'serverid' in request.GET and request.GET.get('serverid'):
            ret = dict(data=list(pms.ItemServer.objects.filter(pk=int(request.GET.get('serverid'))).values(*fields))[0])
            # print(ret)
            return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')
        else:
            ret = dict(data=pms.ItemServer.objects.filter(item_id=request.session['item_id']),b='test')
        return render(request, 'PMsys/pro_list/detail/server_detail.html', ret)

    def post(self, request):
        print(request.POST)
        if 'id' in request.POST and request.POST['id']:
            server = get_object_or_404(pms.ItemServer, pk=int(request.POST['id']))
            server_form = ItemServerForm(request.POST, instance=server)
        else:
            server_form = ItemServerForm(request.POST)
        print(server_form)
        if server_form.is_valid():
            server_form.save()
            ret ={
                'result': 'success'
            }
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(server_form.errors)
            explainform_errors = re.findall(pattern, errors)
            ret = {
                'result': 'fail',
                'massage': explainform_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class ListRelatedView(LoginRequiredMixin, View):
    """项目相关视图"""

    def get(self, request):

        return render(request, 'PMsys/pro_list/detail/pro_detail.html')


class ListDeliView(ListRelatedView, View):
    """库存发货视图"""
    def get(self, request):
        item_goods = pms.ItemGoods.objects.filter(items_id=request.session['item_id']).filter(type=1)
        item_inventory = pms.ItemGoods.objects.filter(items_id=request.session['item_id']).filter(type=2)
        goods_image = pms.GoodsImage.objects.all()
        ret = {
            'item_goods': item_goods,
            'item_inventory':item_inventory,
            'goods_image': goods_image,
        }
        return render(request, 'PMsys/pro_list/detail/deli_detail.html', ret)

    def post(self, request):
        if request.FILES and 'memo' in request.POST and request.POST['memo'] :
            goods = pms.ItemGoods.objects.create(
                items_id=int(request.POST['items']),
                type=request.POST['type'],
                user_id=request.POST['user'],
                memo=request.POST['memo']
            )
            files = request.FILES.getlist('image')
            for file in files:
                # print({'image':file})
                image_form = ImageForm({'goods':goods.id}, {'image':file})
                # print(image_form)
                if image_form.is_valid():
                    image_form.save()
            ret = {
                'result': 'sussecc',
                'msg': '保存成功'
            }
            return HttpResponse(json.dumps(ret), content_type='application/json')
        else:
            ret = {
                'result': 'fail',
                'msg': '发货说明或附件不能为空'
            }
            return HttpResponse(json.dumps(ret), content_type='application/json')


class ListPersonView(ListRelatedView, View):
    """联系人"""

    def get(self, request):
        linkman = pms.ItemLinkman.objects.filter(items_id=int(request.session['item_id']))
        print(linkman)
        ret = {
            'data': linkman
        }
        return render(request, 'PMsys/pro_list/detail/person_detail.html', ret)

    def post(self, request):
        # print(request.POST)
        if 'id' in request.POST and request.POST['id']:
            linkman = get_object_or_404(pms.ItemLinkman, pk=int(request.POST['id']))
            link_form = LinkForm(request.POST, instance=linkman)
        else:
            link_form = LinkForm(request.POST)
        if link_form.is_valid():
            link_form.save()
            # pass
            ret = {
                'result': 'success',
                'msg': '保存成功'
            }
        else:
            ret = {
                'result': 'fail',
                'msg': '保存失败'
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


# 资源管理
class FacilManuView(LoginRequiredMixin, View):
    """厂家信息"""
    def get(self, request):

        ret = dict(data=pms.Manufacturer.objects.all())
        ret['model'] = json.dumps(dict(pms.Manufacturer.FACTURER_TYPE_CHOICE))
        return render(request, 'PMsys/pro_facil/list/manu_info.html', ret)

    def post(self, request):
        if 'id' in request.POST and request.POST['id']:
            manu = get_object_or_404(pms.Manufacturer, pk=int(request.POST['id']))
            manuinfo_form = ManuinfoForm(request.POST, instance=manu)
        else:
            manuinfo_form = ManuinfoForm(request.POST)

        if manuinfo_form.is_valid():
            manuinfo_form.save()
            ret = {'result': 'success'}
        else:
            ret = {'result': 'fail'}
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FacilDevView(LoginRequiredMixin, View):
    """设备信息"""

    def get(self, request):
        fields = ['id', 'title']
        manufacturers = pms.Manufacturer.objects.values(*fields)
        ret = dict(data=pms.WindPower.objects.all())
        ret['manus'] = manufacturers
        ret['manufacturers'] = json.dumps(list(manufacturers))
        return render(request, 'PMsys/pro_facil/list/dev_info.html', ret)

    def post(self, request):

        if 'id' in request.POST and request.POST['id']:
            dev = get_object_or_404(pms.WindPower, pk=int(request.POST['id']))
            dev_form = DevinfoForm(request.POST, instance=dev)
        else:
            dev_form = DevinfoForm(request.POST)

        if dev_form.is_valid():
            dev_form.save()
            ret = {'result': 'success'}
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            ret = {
                'result': 'fail',
                'message':re.findall(pattern, str(dev_form.errors))[0]
            }
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FacilColView(LoginRequiredMixin, View):
    """采集器信息"""

    def get(self, request):
        ret = dict(data=pms.FacilityType.objects.all())
        return render(request, 'PMsys/pro_facil/list/col_info.html', ret)

    def post(self, request):
        print(request.POST)
        if 'id' in request.POST and request.POST['id']:
            facility = get_object_or_404(pms.FacilityType, pk=int(request.POST['id']))
            facility_form = FacilityForm(request.POST, instance=facility)
        else:
            facility_form = FacilityForm(request.POST)
        print(facility_form)
        if facility_form.is_valid():
            facility_form.save()
            ret = {'result': 'success'}
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            ret = {
                'result': 'fail',
                'message':re.findall(pattern, str(facility_form.errors))[0]
            }
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FacilSensorView(LoginRequiredMixin, View):
    """传感器信息"""

    def get(self, request):
        ret = dict(data=pms.SensorType.objects.all())
        return render(request, 'PMsys/pro_facil/list/sensor_info.html', ret)

    def post(self, request):

        print('aaa',request.POST)
        if 'id' in request.POST and request.POST['id']:
            sensor = get_object_or_404(pms.SensorType, pk=int(request.POST['id']))
            sensor_form = SensorForm(request.POST, instance=sensor)
        else:
            sensor_form = SensorForm(request.POST)
        if sensor_form.is_valid():
            sensor_form.save()
            ret = {'result': 'success'}
        else:
            # 这个正则会取出小括号中间的数据
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            ret = {
                'result': 'fail',
                'message':re.findall(pattern, str(sensor_form.errors))[0]
            }
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')


class FacilPasswdView(LoginRequiredMixin, View):

    def get(self, request):
        pwdfile = os.path.join(os.getcwd(),'APPS','utils','tools','passwd.txt')
        if os.path.isfile(pwdfile):
            f = open(pwdfile, 'r')
            a = f.readlines()
            pwd_dict = dict()
            for var in a:
                key, value = var.split(':')
                pwd_dict[key] = value.strip()
            ret = {
                'passwds' : pwd_dict
            }
        else:
            ret = {}
        return render(request, 'PMsys/pro_facil/list/pwd_info.html', ret)