import self as self

from odoo import api, fields, models


class WizardExample(models.TransientModel):
    _name = 'wizard.example'
    _description = 'Example of wizard take data from hms model'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    email = fields.Char('Email')
    birth_date = fields.Date('Birth Date')
    patient_history = fields.Text('History')
    cr_ratio = fields.Float('CR Ratio')
    blood_type = fields.Selection([('a', 'A'), ('b', 'B'), ('ab', 'AB'), ('o', 'O')])

    tag_ids = fields.Many2many('hms.department', string="Tags")

    def action_cancel(self):
        return

    def print_report(self):
        print(self.read()[0])
        data = {
            'form': self.read()[0]
        }
        print('data', data)
        return self.env.ref('iti.wizard_report').report_action(self, data=data)

    # Function to the button
    def update_many2many_field(self):
        self.tag_ids = []
        print(self.tag_ids)
        self.write({'tag_ids': [(1, 0, self.tag_ids)]})
        return



