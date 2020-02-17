from django.db import models

from db.base_model import BaseModel

# Create your models here.


class Items(BaseModel):
    """
    所有业主、主机厂、任务单管理、日志共有的数据表
    """

    ITEMS_TYPE_CHOICE = (
        ('wind', '风电'),
        ('fire', '火电'),
    )

    ITEM_STATUS = (
        ('0', '新建'),
        ('1', '保修期内'),
        ('2', '过保修期'),
    )

    item_type = models.CharField(choices=ITEMS_TYPE_CHOICE, max_length=64, default='wind', verbose_name='项目类型')
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名称')  # 不可重复
    status = models.CharField(choices=ITEM_STATUS, default=0, verbose_name='项目状态')
    address = models.CharField(max_length=64, null=True, blank=True, verbose_name='地址')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='主机厂信息',
                                     on_delete=models.SET_NULL)
    image = models.ImageField(max_length=100, null=True, blank=True, verbose_name='默认图片')
    managerfirm = models.ForeignKey('ManagerFirm', null=True, blank=True, verbose_name='业主信息',
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


class ItemUsers(BaseModel):
    """项目联系人表"""
    pass


class Manufacturer(BaseModel):
    """主机厂信息"""

    name = models.CharField(max_length=64, verbose_name='主机厂名称')
    linkman = models.CharField(max_length=32, null=True, blank=True, verbose_name='主机厂联系人')
    mobile = models.CharField(max_length=11, default='', verbose_name='主机厂联系电话')
    memo = models.CharField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = verbose_name


class ItemServer(models.Model):

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