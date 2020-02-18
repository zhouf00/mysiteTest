from django.db import models
from tinymce.models import HTMLField

from db.base_model import BaseModel

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
        (1, '新建'),
        (2, '保修期内'),
        (3, '过保修期'),
    )

    item_type = models.SmallIntegerField(choices=ITEMS_TYPE_CHOICE, default=1, verbose_name='项目类型')
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名称')  # 不可重复
    status = models.SmallIntegerField(choices=ITEM_STATUS, default=0, verbose_name='项目状态')
    address = models.CharField(max_length=64, null=True, blank=True, verbose_name='地址')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='主机厂信息',
                                     on_delete=models.SET_NULL)
    image = models.ImageField(max_length=100, null=True, blank=True, verbose_name='默认图片')
    managerfirm = models.ForeignKey('ManagerFirm', null=True, blank=True, verbose_name='业主公司',
                                     on_delete=models.SET_NULL)
    entrancetime = models.DateTimeField(verbose_name='入场时间')
    endtime = models.DateTimeField(verbose_name='完成时间')
    accpettime = models.DateTimeField(verbose_name='验收时间')
    facilitycount = models.IntegerField(verbose_name='采集器数量')
    sensorcount = models.IntegerField(verbose_name='传感器数量')

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
    items = models.ForeignKey('Items', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=32, verbose_name='姓名')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='电话')
    status = models.SmallIntegerField(choices=USER_STATUS_CHOICE, default=1, verbose_name='人员状态')
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name='职位')
    wechat = models.CharField(max_length=64, null=True, blank=True, verbose_name='职位')
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

    title = models.CharField(max_length=64, verbose_name='主机厂名称')
    modle = models.SmallIntegerField(choices=FACTURER_TYPE_CHOICE, null=True, blank=True, verbose_name='行业类型')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = verbose_name


class WindPower(BaseModel):
    """风电主机表"""

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    title = models.CharField(max_length=64, verbose_name='风机名称')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='厂商信息',
                                     on_delete=models.SET_NULL)
    model = models.CharField(max_length=64, null=True, blank=True, verbose_name='风机型号')
    nameplate = models.CharField(max_length=64, null=True, blank=True, verbose_name='铭牌')
    height = models.IntegerField(verbose_name='塔筒高度')
    blade_length = models.IntegerField(verbose_name='叶片长度')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '风电主机'
        verbose_name_plural = verbose_name


class ItemsFiles(BaseModel):
    """项目文件表"""

    FILE_TYPE_CHOICE = (
        (1, '入场手续'),
        (2, '验收单'),
        (3, '质量检验单'),
        (4, '其它'),
    )
    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    # title = models.CharField(max_length=32, verbose_name='文件名字')
    type = models.SmallIntegerField(choices=FILE_TYPE_CHOICE, verbose_name='文件类型')
    path = models.FileField(verbose_name='文件位置')

    class Meta:
        verbose_name = '项目文件'
        verbose_name_plural = verbose_name


class ItemsImage(BaseModel):
    """项目图片"""

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='图片')

    class Meta:
        verbose_name = '项目图片'
        verbose_name_plural = verbose_name


class ItemTrip(BaseModel):

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    direction = models.SmallIntegerField(default=0, verbose_name='出行方向')
    city = models.CharField(max_length=32, verbose_name='城市')
    percept = models.TextField(verbose_name='方案')
    # percept = HTMLField(verbose_name='方案详情')

    class Meta:
        verbose_name = '出行表'


class ItemStay(BaseModel):

    items = models.ForeignKey('Items', on_delete=models.CASCADE)
    hoteltitle = models.CharField(max_length=32, verbose_name='酒店名称')
    hosteladdress = models.CharField(max_length=64, verbose_name='酒店地址')



class ItemServer(BaseModel):

    server_type_choice = (
        (0, '浏览站'),
        (1, '塔式服务器'),
        (2, '柜式服务器')
    )

    item = models.ForeignKey('Items', on_delete=models.CASCADE) #
    sn =models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器SN号')
    os_release = models.CharField(max_length=64, null=True, blank=True, verbose_name='操作系统版本')
    soft_release = models.CharField(max_length=64, null=True, blank=True, verbose_name='软件版本')

    def __str__(self):
        return self.sn

    class Meta:
        verbose_name = '服务器信息'


class ServerImage(BaseModel):
    pass



