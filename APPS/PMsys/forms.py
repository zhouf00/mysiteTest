import re
from django import forms
from PMsys import models as pms


class ItemForm(forms.ModelForm):

    class Meta:
        model = pms.Items
        fields = ['id','item_type', 'name', 'x', 'y', 'status', 'address', 'telephone', 'manufacturers',
                 ]
        error_messages = {
            'telephone': {'required': '手机号码不能为空',
                       'max_length': '输入有效的手机号码',
                       'min_length': '输入有效的手机号码'}
        }

    def clean(self):
        cleaned_data = super(ItemForm, self).clean()
        telephone = cleaned_data.get('telephone','')
        # 手机号码合法性验证
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, str(telephone)):
            raise forms.ValidationError('手机号码非法')


class ItemServerForm(forms.ModelForm):

    server_type = forms.IntegerField()
    disk_type = forms.IntegerField()
    raid_type = forms.IntegerField()
    nic1 = forms.GenericIPAddressField()

    class Meta:
        model = pms.ItemServer
        fields = '__all__'


class ManuinfoForm(forms.ModelForm):

    model = forms.IntegerField()

    class Meta:
        model = pms.Manufacturer
        fields = '__all__'


class DevinfoForm(forms.ModelForm):

    class Meta:
        model = pms.WindPower
        fields = '__all__'


class FacilityForm(forms.ModelForm):

    modal = forms.IntegerField()
    chanelnum = forms.IntegerField()

    class Meta:
        model = pms.FacilityType
        fields = '__all__'


class SensorForm(forms.ModelForm):

    class Meta:
        model = pms.SensorType
        fields = '__all__'


class PowerForm(forms.ModelForm):

    status = forms.BooleanField()

    class Meta:
        model = pms.ItemPower
        fields = '__all__'


class ItemFileForm(forms.ModelForm):

    type = forms.IntegerField()

    class Meta:
        model = pms.ItemsFiles
        fields = ['items','file', 'title', 'user', 'type']

    # def chean(self):
    #     cheaned_data = super(ItemFileForm, self).clean()


class StayForm(forms.ModelForm):

    class Meta:
        model = pms.ItemStay
        fields = ['items', 'hoteltitle', 'hoteladdress', 'telephone', 'memo', 'user']
        error_messages = {
            'hoteltitle': {'required': '宾馆名称不能为空'},
            'hoteladdress': {'required': '宾馆地址不能为空'},
            'telephone': {'required': '手机号码不能为空',
                       'max_length': '输入有效的手机号码',
                       'min_length': '输入有效的手机号码'}
        }

    def clean(self):
        cleaned_data = super(StayForm, self).clean()
        telephone = cleaned_data.get('telephone','')
        # 手机号码合法性验证
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        if not re.match(REGEX_MOBILE, str(telephone)):
            raise forms.ValidationError('手机号码非法')


class TripForm(forms.ModelForm):

    class Meta:
        model = pms.ItemTrip
        fields = ['items', 'direction', 'city', 'percept', 'user']
        error_messages = {
            'city': {'required': '目标城市不能为空'},
            'percept': {'required': '出行方案请写详细'},
        }


class ExplainForm(forms.ModelForm):

    type = forms.IntegerField()

    class Meta:
        model = pms.ItemExplain
        fields = ['items', 'user', 'content', 'type']
        error_messages = {
            'content': {'required': '内容不能为空'}
        }


class ImageForm(forms.ModelForm):

    class Meta:
        model = pms.GoodsImage
        fields = ['goods', 'image']


