import json, re, os, datetime
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.core.serializers.json import DjangoJSONEncoder

from utils.mixin_utils import LoginRequiredMixin
from PMsys.forms import ItemFileForm, StayForm, TripForm, ExplainForm
from PMsys import models as pms

from mysiteTest.settings import MEDIA_ROOT


class ProcedureView(LoginRequiredMixin, View):

    def get(self, request):
        # print(request.GET)
        fields = ['id', 'create_time', 'items__name', 'title', 'file', 'memo', 'user__name']
        if 'type' in request.GET and request.GET['type']:
            data = list(pms.ItemsFiles.objects.filter(items_id=request.session['item_id']).filter(type=request.GET['type']).values(*fields))
        else:
            data = None
        for var in data:
            var['create_time'] = (var['create_time']+ datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        ret = {
            'data': data
        }
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

    def post(self, request):
        ret = dict()
        file = request.FILES.get('file', None)
        if not file:
            ret['result'] = 'fail'
            ret['msg'] = '没有文件'
            return HttpResponse(json.dumps(ret), content_type='application/json')
        file_form = ItemFileForm(request.POST, request.FILES)
        # print(file_form)
        if file_form.is_valid():
            dir = str(file_form.cleaned_data['items'])
            file = str(file_form.cleaned_data['file'])
            newfile = os.path.join(MEDIA_ROOT, dir, file)
            if os.path.exists(newfile):
                ret['result'] = 'fail'
                ret['msg'] = '<%s>文件已经存在，不要重复上传'%file
            else:
                file_form.save()
                ret['result'] = 'sussecc'
                ret['msg'] = '文件上传成功'
        else:
            ret['result'] = 'fail'
            ret['msg'] = '有错误'
        return HttpResponse(json.dumps(ret), content_type='application/json')


class StayView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'create_time', 'items__name', 'hoteltitle', 'hoteladdress',
                  'telephone', 'memo', 'user__name']
        data = list(pms.ItemStay.objects.filter(items_id=request.session['item_id']).values(*fields))
        for var in data:
            var['create_time'] = (var['create_time']+ datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        ret = {
            'data': data
        }
        return HttpResponse(json.dumps(ret, cls=DjangoJSONEncoder), content_type='application/json')

    def post(self, request):
        stay_form = StayForm(request.POST)

        if stay_form.is_valid():
            stay_form.save()
            ret = {
                'result': 'sussecc',
                'msg': '保存成功'
            }
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(stay_form.errors)
            stayform_errors = re.findall(pattern, errors)
            ret = {
                'result': 'fail',
                'msg': stayform_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class TripView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'create_time', 'items__name', 'direction', 'city',
                  'percept', 'user__name']
        data = list(pms.ItemTrip.objects.filter(items_id=request.session['item_id']).values(*fields))
        print(data)
        for var in data:
            var['create_time'] = (var['create_time']+ datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        ret = {
            'data': data
        }
        return HttpResponse(json.dumps(ret), content_type='application/json')

    def post(self, request):
        trip_form = TripForm(request.POST)
        if trip_form.is_valid():
            trip_form.save()
            ret = {
                'result': 'sussecc',
                'msg': '保存成功'
            }
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(trip_form.errors)
            stayform_errors = re.findall(pattern, errors)
            ret = {
                'result': 'fail',
                'msg': stayform_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class TrafficView(LoginRequiredMixin, View):

    def get(self, request):
        pass

    def post(self, request):
        pass


class ExplainView(LoginRequiredMixin, View):

    def get(self, request):
        fields = ['id', 'create_time', 'items__name', 'type', 'content',
                  'user__name']
        data = list(pms.ItemExplain.objects.filter(items_id=request.session['item_id']).values(*fields))
        print(data)
        for var in data:
            var['create_time'] = (var['create_time'] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
        ret = {
            'data': data
        }
        return HttpResponse(json.dumps(ret), content_type='application/json')

    def post(self, request):
        explain_form = ExplainForm(request.POST)
        print(explain_form)
        if explain_form.is_valid():
            explain_form.save()
            ret = {
                'result': 'sussecc',
                'msg': '保存成功'
            }
        else:
            pattern = '<li>.*?<ul class=.*?><li>(.*?)</li>'
            errors = str(explain_form.errors)
            explainform_errors = re.findall(pattern, errors)
            ret = {
                'result': 'fail',
                'msg': explainform_errors[0]
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')


class FileDeleteView(LoginRequiredMixin, View):
    """删除文件"""

    def post(self, request):
        id_nums = request.POST['id']
        d_file = pms.ItemsFiles.objects.filter(id=id_nums)
        if d_file.exists():
            d_file = d_file[0]
            d_file.delete()
            d_file_name = str(d_file.file)
            d_file_name = os.path.join(MEDIA_ROOT, d_file_name)
            if os.path.exists(d_file_name):
                os.remove(d_file_name)
            ret = {
                'result': 'true',
                'message': '数据删除成功！'
            }
        else:
            ret = {
                'result': 'false',
                'message': '文件不存在！'
            }
        return HttpResponse(json.dumps(ret), content_type='application/json')

