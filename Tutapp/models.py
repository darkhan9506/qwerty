from django.db import models
from treebeard.mp_tree import MP_Node


class Departments(MP_Node):
    title = models.CharField(max_length = 100)

    node_order_by = ['title']

    def __unicode__(self):
        return 'Category: %s' % self.title


class Employees(models.Model):
    name = models.CharField(max_length = 100)
    code = models.IntegerField()
    position = models.CharField(max_length = 100)
    department = models.ManyToManyField(Departments, related_name='employees')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
