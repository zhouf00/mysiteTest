import json
from PMsys.models import ItemPower, ItemSensors, ItemFacilitys,Items, WindPower


class NewPower:
    # 风机的新建

    def __init__(self, request, p=1):
        self.request = request
        self.sensors = json.loads((request.POST['sensors']))
        self.p = p
        # self.power_upline()

    def power_upline(self):
        newpower = self._create_itempower()
        newfacility = self._create_itemfacility(newpower)
        self._create_itemsenor(newfacility)

    def power_del(self):
        newpower = ItemPower.objects.filter(pk=int(self.request.POST['powerId']))
        newpower.delete()

    def _create_itempower(self):
        # print('保存风机')
        if self.p:
            newpower = ItemPower.objects.filter(pk=int(self.request.POST['powerId']))[0]
            newpower.items_id = self.request.session['item_id']
            newpower.windpower = WindPower(self.request.POST['windpower'])
            newpower.p_title = self.request.POST['p_title']
            newpower.status = self.request.POST['status']
            newpower.save()

        else:
            p = ItemPower.objects.filter(items=self.request.session['item_id'], p_title=self.request.POST['p_title'])
            if p:
                raise Exception('风机已经存在')

            newpower = ItemPower.objects.create(
                items=Items(self.request.session['item_id']),
                windpower_id=self.request.POST['windpower'],
                p_title=self.request.POST['p_title'],
                status=self.request.POST['status']
            )
        return newpower

    def _create_itemfacility(self, newpower):
        # print('保存采集器')
        f = ItemFacilitys.objects.filter(itempower=newpower, ip=self.request.POST['ip'])
        if f:
            newfacility = f[0]
            newfacility.itempower = newpower
            newfacility.facilitys_id = self.request.POST['facility']
            newfacility.f_title = self.request.POST['f_title']
            newfacility.soft_version = self.request.POST['soft_version']
            newfacility.hardware_version = self.request.POST['hardware_version']
            newfacility.save()
        else:
            try:
                newfacility = ItemFacilitys.objects.create(
                    itempower=newpower,
                    facilitys_id=self.request.POST['facility'],
                    f_title=self.request.POST['f_title'],
                    ip=self.request.POST['ip'],
                    soft_version=self.request.POST['soft_version'],
                    hardware_version=self.request.POST['hardware_version'],
                )
            except:
                newpower.delete()
                raise Exception('采集器未选择')
        return newfacility

    def _create_itemsenor(self, newfacility):
        # print('保存传感器')
        newfacility.sensors.clear()

        for newsensor in self.sensors:
            # print(newsensor)
            # s = ItemSensors.objects.filter(itemfacility=newfacility, s_title=newsensor['number'])

            ItemSensors.objects.create(
                itemfacility=newfacility,
                number=newsensor['number'],
                sensor_id=newsensor['sensor'],
                s_title=newsensor['s_title'],
                install_site=newsensor['install_site']
            )
