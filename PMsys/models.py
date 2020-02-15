from django.db import models

# Create your models here.


class Items(models.Model):
    """
    所有业主、主机厂、任务单管理、日志共有的数据表
    """

    item_type_choice = (
        ('wind', '风电'),
        ('fire', '火电'),
    )

    item_status = (
        ('0', '新建'),
        ('1', '保修期内'),
        ('2', '过保修期'),
    )

    item_type = models.CharField(choices=item_type_choice, max_length=64, default='wind', verbose_name='项目类型')
    name = models.CharField(max_length=64, unique=True, verbose_name='项目名称')  # 不可重复
    sn = models.CharField(max_length=128, unique=True, verbose_name='项目编号')  # 不可重复
    status = models.CharField(choices=item_status, default=0, verbose_name='项目状态')
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, verbose_name='主机厂信息',
                                     on_delete=models.SET_NULL)
    managerment = models.ForeignKey('Managerment', null=True, blank=True, verbose_name='业主信息',
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name


class Managerment(models.Model):
    """
    业主信息
    """

    name = models.CharField(max_length=64, verbose_name='业主名称')
    about = models.TextField(verbose_name='简介')
    linkman = models.CharField(max_length=32, null=True, blank=True, verbose_name='业主联系人')
    mobile = models.CharField(max_length=11, default='', verbose_name='业主联系电话')
    memo = models.CharField(null=True, blank=True, verbose_name='备注')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = verbose_name


class Manufacturer(models.Model):
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