# -*-coding: utf-8
#from . import models,fields,api

from odoo import  models,fields,api

class demo_test(models.Model):
    _name="test_demo.test_demo"

    name= fields.Char(string="first name", required= True )
    age=fields.Integer(string="Age", required =True)
    birthdate=fields.Date(required=True)
   # name=fields.