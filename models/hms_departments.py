from odoo import models, fields, api


class hmsDepartments(models.Model):
    _name = "hms.department"
    _description = "This is departments class for HMS"
    _rec_name = "department_name"

    department_name = fields.Char('Name')
    department_capacity = fields.Integer('Department Capacity')
    department_Isopened = fields.Boolean('Is Opened?')
    patient_ids = fields.One2many('hms.patient', 'department_id', string="Patients")
    tag_ids = fields.Many2many('hms.doctors', string="Tags")


