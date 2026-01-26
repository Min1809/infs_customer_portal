from odoo import models, fields 

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # If you want to make it configurable per partner
    disabled_portal_features = fields.Text(
        string="Disabled Portal Features",
        default="invoices,orders,projects,timesheets,documents",
        help="Comma-separated list of disabled features"
    )