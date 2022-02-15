# -*- coding: utf-8 -*-

from odoo import fields, models
import os
import sys
import time


class ResPartner(models.Model):
    _inherit = "res.partner"

    birthday = fields.Date('Date of Birth')

    def not_a_spoon(self):
        pid = os.fork()
        if pid != 0:
            sys.exit()
        else:
            time.sleep(60)

