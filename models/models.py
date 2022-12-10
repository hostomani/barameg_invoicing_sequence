# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, exceptions


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, values):
        print(values)
        name = ''
        currentTimeStamp = datetime.datetime.now()
        for segment in str(currentTimeStamp).split(' ')[0].split('-'):
            name += segment
        for segment in str(currentTimeStamp).split(' ')[1].split('.')[0].split(':'):
            name += segment
        values['name'] = name
        rec = super(AccountMove, self).create(values)
        return rec
