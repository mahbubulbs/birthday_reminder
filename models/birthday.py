from odoo import models, fields

class BirthdayReminder(models.Model):
    _name = "birthday.reminder"
    _description = "Birthday Reminder"

    name = fields.Char(required=True)
    birth_date = fields.Date(required=True)