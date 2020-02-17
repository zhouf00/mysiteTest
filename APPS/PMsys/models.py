from django.db import models

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

    item_type = models.SmallIntegerField(choices=ITEMS_TYPE_CHOICE, max_length=64, default='wind', verbose_name='项目类型')
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
    items = models.ForeignKey('Items', on_delete=models.SET_NULL)
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

    name = models.CharField(max_length=64, verbose_name='主机厂名称')
    linkman = models.CharField(max_length=32, null=True, blank=True, verbose_name='主机厂联系人')
    mobile = models.CharField(max_length=11, default='', verbose_name='主机厂联系电话')
    memo = models.TextField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = verbose_name


class WindPower(BaseModel):
    """风电主机表"""
    ITEMS_TYPE_CHOICE = (
        (1, '风电'),
        (2, '火电'),
    )

    items = models.ForeignKey('Items', on_delete=models.SET_NULL)
    title = models.CharField(max_length=64, verbose_name='风机名称')




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