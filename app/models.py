from django.db import models

class category1_tbl(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    isactive = models.CharField(max_length=200,blank=True, null=True)
    created =  models.DateField(null=True, blank=True)
    path = models.CharField(max_length=1000,blank=True, null=True)
    modify = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=1000,blank=True, null=True)

class priority_tbl(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)
    isactive = models.CharField(max_length=200,blank=True, null=True)
    created =  models.DateField(null=True, blank=True)
    modify = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=200,blank=True, null=True)

class category2_tbl(models.Model):
    category1 = models.ForeignKey(category1_tbl, models.DO_NOTHING, blank=True, null=True)
    priority = models.ForeignKey(priority_tbl, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200,blank=True, null=True)
    isactive = models.CharField(max_length=200,blank=True, null=True)
    created =  models.DateField(null=True, blank=True)
    modify = models.DateField(null=True, blank=True)
    created_by = models.CharField(max_length=200,blank=True, null=True)

class card_tbl(models.Model):
    category1 = models.ForeignKey(category1_tbl, models.DO_NOTHING, blank=True, null=True)
    category2 = models.ForeignKey(category2_tbl, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.CharField(max_length=1500,blank=True, null=True)
    requested_by = models.CharField(max_length=200,blank=True, null=True)
    path = models.CharField(max_length=1000,blank=True, null=True)
    date_requested = models.DateField(null=True, blank=True)
    status = models.IntegerField(max_length=60, default=0, null=True)

class roles_tbl(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True)

class user_tbl(models.Model):
    roles = models.ForeignKey(roles_tbl, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200,blank=True, null=True)

class assigned_tbl(models.Model):
    user = models.ForeignKey(user_tbl, models.DO_NOTHING,blank=True, null=True)
    task = models.ForeignKey(card_tbl, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200,blank=True, null=True)

class folder_tbl(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True)
    date_upload = models.DateField(null=True, blank=True)
    class Meta:
        db_table = "folder_tbl"

class gallery_photos(models.Model):
    card_id = models.IntegerField()
    photos = models.FileField(upload_to='Photos/', unique=True)





