from django.db import models

class User(models.Model):
    s_username=models.CharField('用户名',max_length=20,unique=True)
    s_password=models.CharField('密码',max_length=20)
    n_phonenumber=models.IntegerField('手机号')
    s_mail=models.EmailField('邮箱',max_length=30)
    class Meta:
        db_table='doc_users'
class Doc(models.Model):
    """
    文件模型
    """
    s_file_url = models.URLField('文件url', help_text='文件url')
    s_file_name = models.CharField('文件名', max_length=48,  help_text='文件名')
    s_title = models.CharField('文件标题', max_length=150, help_text='文件标题')
    s_desc = models.TextField('文件描述', help_text='文件描述')
    s_image_url = models.URLField('封面图片url', help_text='封面图片url')
    n_doc_type=models.SmallIntegerField('文件类型',choices=((1,'PDF'),(2,'WORD'),(3,'EXCEL'),(4,'PPT'),(5,'Other')))
    class Meta:
        db_table = 'doc_filelist'        # 数据库表名
        verbose_name = '文件表'        # admin 站点中显示的名称
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
class Privilege(models.Model):
    s_username=models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 to_field='s_username',
                                 related_name='user_privilege')
    chinese=models.SmallIntegerField()
    math=models.SmallIntegerField()
    english=models.SmallIntegerField()
    class Meta:
        db_table='doc_privilege'