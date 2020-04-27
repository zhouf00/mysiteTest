from django.db import models
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField

from db.base_model import BaseModel

User = get_user_model()


# Create your models here.


class Items(BaseModel):
    """
    所有业主、主机厂、任务单管理、日志共有的数据表
    """
    ITEMS_TYPE_CHOICE = (
        (1, '风电'),
        (2, '火电'),
    )

    ITEM_STATUS = (
        (1, '未开工'),
        (2, '安装中'),
        (3, '维护中'),
        (4, '质保内'),
        (5, '过保'),
        (6, '待维护'),
    )

    item_type = models.SmallIntegerField(choices=ITEMS_TYPE_CHOICE, default=1, verbose_name='项目类型')
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名称')  # 不可重复
    x = models.FloatField(verbose_name='坐标x')
    y = models.FloatField(  verbose_name='坐标y')
    status = models.SmallIntegerField(choices=ITEM_STATUS, default=0, verbose_name='项目状态')
    address = models.CharField(max_length=64, null=True, blank=True, verbose_name='地址')
    telephone = models.CharField(max_length=16, null=True, blank=True, verbose_name='值班电话')
    image = models.ImageField(max_length=100, null=True, blank=True, verbose_name='默认图片')
    managerfirm = models.ForeignKey('ManagerFirm', null=True, blank=True, verbose_name='业主公司',
                                    on_delete=models.SET_NULL)
    manufacturers = models.ManyToManyField('Manufacturer', blank=True, verbose_name='主机厂信息')
    powers = models.ManyToManyField('WindPower', blank=True, through='ItemPower',
                                    through_fields=('items', 'windpower') )
    entrancetime = models.DateTimeField(null=True, blank=True, verbose_name='入场时间')
    endtime = models.DateTimeField(null=True, blank=True, verbose_name='完成时间')
    accpettime = models.DateTimeField(null=True, blank=True, verbose_name='验收时间')
    facilitycount = models.IntegerField(null=True, blank=True, verbose_name='采集器数量')
    sensorcount = models.IntegerField(null=True, blank=True, verbose_name='传感器数量')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name


class ManagerFirm(BaseModel):
    """
    项目管理公司
    """

    name = models.CharField(max_length=64, verbose_name='管理公司名称')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目管理公司'
        verbose_name_plural = verbose_name


class ItemLinkman(BaseModel):
    """项目联系人表"""
    USER_STATUS_CHOICE = (
        (1, '在岗'),
        (2, '休假'),
        (3, '离职'),
    )
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    status = models.SmallIntegerField(choices=USER_STATUS_CHOICE, default=1, verbose_name='人员状态')
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name='职位')
    wechat = models.CharField(max_length=64, null=True, blank=True, verbose_name='微信')
    mail = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    is_managerfirm = models.BooleanField(default=False, verbose_name='是否为业主')
    befirm = models.CharField(max_length=64, null=True, blank=True, verbose_name='所属单位')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目联系人'
        verbose_name_plural = verbose_name


class Manufacturer(BaseModel):
    """主机厂信息"""
    FACTURER_TYPE_CHOICE = (
        (1, '风电'),
        (2, '火电'),
    )

    title = models.CharField(max_length=64, unique=True, verbose_name='主机厂名称')
    model = models.SmallIntegerField(choices=FACTURER_TYPE_CHOICE, default=1, null=True, blank=True,
                                     verbose_name='行业类型')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = verbose_name


class WindPower(BaseModel):
    """风电主机表"""

    title = models.CharField(max_length=64, null=True, blank=True, verbose_name='风机型号')
    manufacturer = models.ForeignKey('Manufacturer', verbose_name='厂商信息',
                                     on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True, verbose_name='塔筒高度')
    blade_length = models.FloatField(null=True, blank=True, verbose_name='叶片长度')
    tier = models.FloatField(null=True, blank=True, verbose_name='塔筒层数')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '风电主机'
        verbose_name_plural = verbose_name


def upload_path(instance, filename):
    print(instance.items, filename)
    return '/'.join([str(instance.items), filename])


class ItemsFiles(BaseModel):
    """项目文件表"""

    FILE_TYPE_CHOICE = (
        (1, '入场手续'),
        (2, '验收单'),
        (3, '质量检验单'),
        (4, '其它'),
    )
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='文件名字')
    type = models.SmallIntegerField(choices=FILE_TYPE_CHOICE, null=True, blank=True, verbose_name='文件类型')
    file = models.FileField(upload_to=upload_path, unique=True, verbose_name='文件位置')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='填写人')

    class Meta:
        verbose_name = '项目文件'
        verbose_name_plural = verbose_name


class ItemsImage(BaseModel):
    """项目图片"""

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items', verbose_name='图片')

    class Meta:
        verbose_name = '项目图片'
        verbose_name_plural = verbose_name


class ItemTrip(BaseModel):
    """交通表"""
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    direction = models.SmallIntegerField(default=0, verbose_name='出行方向')
    city = models.CharField(max_length=32, verbose_name='城市')
    percept = models.TextField(verbose_name='方案')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='填写人')

    # percept = HTMLField(verbose_name='方案详情')

    class Meta:
        verbose_name = '出行表'


class ItemStay(BaseModel):
    """住宿表"""

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    hoteltitle = models.CharField(max_length=32, verbose_name='酒店名称')
    hoteladdress = models.CharField(max_length=64, verbose_name='酒店地址')
    telephone = models.CharField(max_length=15, verbose_name='酒店电话')
    memo = models.TextField(null=True, blank=True, verbose_name='备注说明')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='填写人')

    class Meta:
        verbose_name = '住宿表'
        verbose_name_plural = verbose_name


class ItemExplain(BaseModel):

    EXP_TYPE_CHOICE = (
        (1, '工具借用'),
        (2, '其它')
    )

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    type = models.SmallIntegerField(choices=EXP_TYPE_CHOICE, verbose_name='文件类型')
    content = models.TextField(verbose_name='内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='填写人')

    class Meta:
        verbose_name = '工具借用'
        verbose_name_plural = verbose_name


class ItemCar(BaseModel):
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    name = models.CharField(max_length=32, verbose_name='联系人')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    invoice = models.BooleanField(default=False, verbose_name='是否提供发票')
    firm = models.CharField(max_length=64, null=True, blank=True, verbose_name='公司名称')
    cost = models.IntegerField(verbose_name='收费标准')

    class Meta:
        verbose_name = '租车表'
        verbose_name_plural = verbose_name


class ItemExecutr(BaseModel):
    """项目施工人信息"""

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='施工人员')
    status = models.SmallIntegerField(verbose_name='施工人员状态')
    begintime = models.DateTimeField(verbose_name='开始时间')
    endtime = models.DateTimeField(verbose_name='结束时间')

    class Meta:
        verbose_name = '施工人员表'
        verbose_name_plural = verbose_name


class PersonTrack(BaseModel):

    name = models.CharField(max_length=32, verbose_name='人员名字')
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    status = models.SmallIntegerField(verbose_name='施工人员状态')
    begintime = models.DateTimeField(verbose_name='开始时间')


class ItemServer(BaseModel):
    """服务器信息"""
    SERVER_TYPE_CHOICE = (
        (1, '浏览站'),
        (2, '塔式服务器'),
        (3, '柜式服务器')
    )
    DISK_TYPE_CHOICE = (
        (1, 'SAS'),
        (2, 'SATA'),
    )
    RAID_TYPE_CHOICE = (
        (0, 'RAID0'),
        (1, 'RAID1'),
        (5, 'RAID5')
    )

    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    server_type = models.SmallIntegerField(choices=SERVER_TYPE_CHOICE, default=1, verbose_name='服务器类型')
    server_model = models.CharField(max_length=64, null=True, blank=True, verbose_name='服务器型号')
    sn = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器SN号')
    os_release = models.CharField(max_length=64, null=True, blank=True, verbose_name='操作系统版本')
    soft_release = models.CharField(max_length=64, null=True, blank=True, verbose_name='软件版本')
    cpu = models.CharField(max_length=64, null=True, blank=True, verbose_name='cpu信息')
    cpu_count = models.SmallIntegerField(null=True, blank=True, default=1, verbose_name='cpu个数')
    ram = models.IntegerField(null=True, blank=True, verbose_name='内存大小')  # 单位G
    disk_type = models.SmallIntegerField(null=True, blank=True, choices=DISK_TYPE_CHOICE, default=1,
                                         verbose_name='硬盘类型')
    disk_size = models.IntegerField(null=True, blank=True, verbose_name='硬盘大小')
    disk_unit = models.SmallIntegerField(verbose_name='硬盘单位')
    disk_count = models.SmallIntegerField(null=True, blank=True, default=1, verbose_name='硬盘个数')
    raid_type = models.SmallIntegerField(null=True, blank=True, default=0, choices=RAID_TYPE_CHOICE, verbose_name='阵列')
    nic1 = models.GenericIPAddressField(null=True, blank=True, verbose_name='网卡1')
    nic2 = models.GenericIPAddressField(null=True, blank=True, verbose_name='网卡2')
    nic3 = models.GenericIPAddressField(null=True, blank=True, verbose_name='网卡3')
    nic4 = models.GenericIPAddressField(null=True, blank=True, verbose_name='网卡4')
    place = models.CharField(max_length=128, null=True, blank=True, verbose_name='放置位置')
    pc_username = models.CharField(max_length=32, null=True, blank=True, verbose_name='电脑帐号')
    pc_passwd = models.CharField(max_length=32, null=True, blank=True, verbose_name='电脑密码')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.server_model

    class Meta:
        verbose_name = '服务器信息'
        verbose_name_plural = verbose_name


# class CPU(models.Model):
#
#     cpu_model = models.CharField(max_length=128, blank=True, null=True, verbose_name='CPU型号')
#     cpu_count = models.PositiveSmallIntegerField(default=1, verbose_name='物理CPU个数')
#     cpu_core_count = models.PositiveSmallIntegerField(default=1, verbose_name='CPU核数')
#
#     class Meta:
#         verbose_name = 'CPU'
#         verbose_name_plural = verbose_name


# class NIC(models.Model):
#
#     server = models.ForeignKey('ItemServer', on_delete=models.CASCADE, verbose_name='服务器')
#     title = models.CharField(max_length=32, verbose_name='网卡名称')
#     ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP地址')
#     netmask = models.CharField(max_length=64, null=True, blank=True, verbose_name='掩码')
#     gateway = models.GenericIPAddressField(null=True, blank=True, verbose_name='网关')
#     bonding = models.CharField(max_length=128, null=True, blank=True, verbose_name='绑定位置')
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = '网卡'
#         verbose_name_plural = verbose_name


class ServerImage(BaseModel):
    """服务器图片"""

    server = models.ForeignKey('ItemServer', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='server', verbose_name='图片')

    class Meta:
        verbose_name = '服务器图片'
        verbose_name_plural = verbose_name


class FacilityType(BaseModel):
    """采集器类型表"""
    MODAL_TYPE_CHOICE = (
        (1, '振动监测'),
        (2, '油液监测'),
    )
    title = models.CharField(max_length=32, verbose_name='采集器型号名称')
    modal = models.SmallIntegerField(choices=MODAL_TYPE_CHOICE,default=1, verbose_name='采集器类型')
    chanelnum = models.SmallIntegerField(verbose_name='通道数')
    memo = models.TextField(null=True, blank=True, verbose_name='详情')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '采集器类型'
        verbose_name_plural = verbose_name


class SensorType(BaseModel):
    """传感器类型"""

    title = models.CharField(max_length=32, unique=True, verbose_name='传感器名称')
    manufacturer = models.CharField(max_length=64, null=True, blank=True, verbose_name='传感器厂商')
    bias_voltage = models.CharField(max_length=32, null=True, blank=True, verbose_name='偏置电压')
    memo = models.TextField(null=True, blank=True, verbose_name='详情')

    class Meta:
        verbose_name = '传感器类型'
        verbose_name_plural = verbose_name


class ItemGoods(BaseModel):
    """库存发货信息"""
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    type = models.SmallIntegerField(verbose_name='类型') # 1：发货   2：库存
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发货人')
    memo = models.TextField(verbose_name='发货说明')

def upload_path_image(instance, filename):
    # print(instance.items, filename)
    return '/'.join([str(instance.goods.items),'img', filename])

class GoodsImage(BaseModel):
    """发货图片"""

    goods = models.ForeignKey('ItemGoods', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_image, verbose_name='发货图片')


class Personnel(BaseModel):
    """人员情况表"""

    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='人员名称')
    status = models.SmallIntegerField(verbose_name='人员状态')

    class Meta:
        verbose_name = '人员情况'
        verbose_name_plural = verbose_name


class WorkLog(BaseModel):
    item = models.ForeignKey('Items', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='填写人')
    status = models.SmallIntegerField(default=0, verbose_name='状态')
    logged = models.TextField(verbose_name='已执行')
    plan = models.TextField(verbose_name='计划')

    class Meta:
        verbose_name = '工作日志'
        verbose_name_plural = verbose_name


class ItemPower(BaseModel):
    """
    项目风机信息表
    项目-风机 中间表
    """

    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    windpower = models.ForeignKey(WindPower, on_delete=models.CASCADE)
    p_title = models.CharField(max_length=64, verbose_name='主机名称')
    facilitys = models.ManyToManyField('FacilityType', through='ItemFacilitys', through_fields=('itempower', 'facilitys'))
    status = models.BooleanField(verbose_name='风机状态')
    nameplate = models.CharField(max_length=64, null=True, blank=True, verbose_name='铭牌')

    def __str__(self):
        return self.p_title

    class Meta:
        verbose_name = '项目风机信息表'


class ItemFacilitys(BaseModel):
    """
    项目采集器信息表
    风机表-采集器 中间表
    """
    itempower = models.ForeignKey(ItemPower, on_delete=models.CASCADE)
    facilitys = models.ForeignKey(FacilityType, on_delete=models.CASCADE)
    f_title = models.CharField(max_length=64, verbose_name='采集器编号')
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name='IP地址')
    soft_version = models.CharField(max_length=64, null=True, blank=True, verbose_name='嵌入式版本')
    hardware_version = models.CharField(max_length=64, null=True, blank=True, verbose_name='硬件版本')
    sensors = models.ManyToManyField('SensorType', through='ItemSensors', through_fields=('itemfacility', 'sensor'))

    def __str__(self):
        return self.f_title


class ItemSensors(BaseModel):
    """项目传感器信息表"""

    itemfacility = models.ForeignKey('ItemFacilitys', on_delete=models.CASCADE)
    sensor = models.ForeignKey('SensorType', on_delete=models.CASCADE)
    number = models.CharField(max_length=32, verbose_name='通道编号')
    s_title = models.CharField(max_length=128, null=True,verbose_name='传感器编号')
    install_site = models.CharField(max_length=128, null=True, blank=True, verbose_name='安装位置')

    def __str__(self):
        return self.s_title



