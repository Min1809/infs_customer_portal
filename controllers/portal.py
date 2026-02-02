from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError


class CustomPortal(CustomerPortal):

    def _show_feature_disabled_message(self):
        """Helper method to show disabled feature message"""
        return request.render(
            "infs_customer_portal.portal_feature_disabled",
            {
                "page_name": "feature_disabled",
            },
        )

    # Sales Orders
    @http.route(
        ["/my/orders", "/my/orders/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_orders(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_orders(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )

        return self._show_feature_disabled_message()

    @http.route(["/my/orders/<int:order_id>"], type="http", auth="public", website=True)
    def portal_order_page(
        self,
        order_id,
        report_type=None,
        access_token=None,
        message=False,
        download=False,
        **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_order_page(
                order_id,
                report_type=report_type,
                access_token=access_token,
                message=message,
                download=download,
                **kw
            )
        return self._show_feature_disabled_message()

    # Quotations
    @http.route(
        ["/my/quotes", "/my/quotes/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_quotes(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_quotes(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )
        return self._show_feature_disabled_message()

    @http.route(
        ["/my/quotes/<int:quotation_id>"], type="http", auth="public", website=True
    )
    def portal_quote_page(
        self,
        quotation_id,
        report_type=None,
        access_token=None,
        message=False,
        download=False,
        **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_quote_page(
                quotation_id,
                report_type=report_type,
                access_token=access_token,
                message=message,
                download=download,
                **kw
            )
        return self._show_feature_disabled_message()

    # Customer Invoices
    @http.route(
        ["/my/invoices", "/my/invoices/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_invoices(
        self, page=1, date_begin=None, date_end=None, sortby=None, filterby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_invoices(
                page=page,
                date_begin=date_begin,
                date_end=date_end,
                sortby=sortby,
                filterby=filterby,
                **kw
            )
        return self._show_feature_disabled_message()

    @http.route(
        ["/my/invoices/<int:invoice_id>"], type="http", auth="public", website=True
    )
    def portal_my_invoice_detail(
        self, invoice_id, access_token=None, report_type=None, download=False, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_invoice_detail(
                invoice_id,
                access_token=access_token,
                report_type=report_type,
                download=download,
                **kw
            )
        return self._show_feature_disabled_message()

    # Vendor Bills (Our Invoices)
    @http.route(
        ["/my/bills", "/my/bills/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_bills(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_bills(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )
        return self._show_feature_disabled_message()

    @http.route(
        ["/my/bills/<int:invoice_id>"], type="http", auth="public", website=True
    )
    def portal_my_bill_detail(
        self, invoice_id, access_token=None, report_type=None, download=False, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_bill_detail(
                invoice_id,
                access_token=access_token,
                report_type=report_type,
                download=download,
                **kw
            )
        return self._show_feature_disabled_message()

    # Purchase Orders (Our Orders)
    @http.route(
        ["/my/purchase", "/my/purchase/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_purchase_orders(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_purchase_orders(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )
        return self._show_feature_disabled_message()

    @http.route(
        ["/my/purchase/<int:order_id>"], type="http", auth="public", website=True
    )
    def portal_my_purchase_order(self, order_id=None, access_token=None, **kw):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_purchase_order(
                order_id=order_id, access_token=access_token, **kw
            )
        return self._show_feature_disabled_message()

    # Projects
    @http.route(
        ["/my/projects", "/my/projects/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_projects(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_projects(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )
        return self._show_feature_disabled_message()

    @http.route(
        ["/my/project/<int:project_id>", "/my/project/<int:project_id>/<path:subpath>"],
        type="http",
        auth="public",
        website=True,
    )
    def portal_my_project(self, project_id=None, access_token=None, **kw):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_project(
                project_id=project_id, access_token=access_token, **kw
            )
        return self._show_feature_disabled_message()

    # Tasks
    @http.route(
        ["/my/tasks", "/my/tasks/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_tasks(
        self,
        page=1,
        date_begin=None,
        date_end=None,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_tasks(
                page=page,
                date_begin=date_begin,
                date_end=date_end,
                sortby=sortby,
                filterby=filterby,
                search=search,
                search_in=search_in,
                **kw
            )
        return self._show_feature_disabled_message()

    @http.route(["/my/task/<int:task_id>"], type="http", auth="public", website=True)
    def portal_my_task(self, task_id, access_token=None, **kw):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_task(task_id, access_token=access_token, **kw)
        return self._show_feature_disabled_message()

    # Timesheets
    @http.route(
        ["/my/timesheets", "/my/timesheets/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_timesheets(
        self,
        page=1,
        sortby=None,
        filterby=None,
        search=None,
        search_in="content",
        groupby="project",
        **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_timesheets(
                page=page,
                sortby=sortby,
                filterby=filterby,
                search=search,
                search_in=search_in,
                groupby=groupby,
                **kw
            )
        return self._show_feature_disabled_message()

    # Subscriptions
    @http.route(
        ["/my/subscriptions", "/my/subscriptions/page/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_subscriptions(
        self, page=1, date_begin=None, date_end=None, sortby=None, **kw
    ):
        if request.env.user.has_group("base.group_user"):
            return super().portal_my_subscriptions(
                page=page, date_begin=date_begin, date_end=date_end, sortby=sortby, **kw
            )
        return self._show_feature_disabled_message()

    # Account editing - allow viewing but not editing
    @http.route(["/my/account"], type="http", auth="user", website=True)
    def account(self, redirect=None, **post):
        if request.httprequest.method == "POST":
            return self._show_feature_disabled_message()
        return super(CustomPortal, self).account(redirect=redirect, **post)

    # Allow home page and security page - keep existing
    @http.route(["/my/home"], type="http", auth="user", website=True)
    def home(self, **kwargs):
        # Allow home page but filter out counters for disabled features
        response = super(CustomPortal, self).home(**kwargs)
        return response

    # FAQ Page
    # @http.route(['/faqs'], type='http', auth="public", website=True)
    # def portal_faqs(self, **kw):
    #     """FAQ page that opens in new tab"""
    #     return request.render('infs_project.portal_faqs', {
    #         'page_name': 'faqs',
    #     })

    # Security page is allowed by default (not overridden)
    # Tickets are allowed by default (not overridden)
