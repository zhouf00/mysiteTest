import re
from django import forms
from PMsys import models as pms


class ItemForm(forms.ModelForm):

    class Meta:
        model = pms.Items
        # fields = '__all__'
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

    file_field = forms.FloatField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

