# Copyright 2020 Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Product Information Management",
    "version": "12.0.1.1.2",
    "license": "AGPL-3",
    "author": "Akretion",
    "website": "http://www.akretion.com/",
    "depends": [
        "attribute_set_searchable",
        "product",
        "product_attribute_set",
        # "product_attribute_set_completeness",
    ],
    "data": [
        "data/ir_module_category_data.xml",
        "security/pim_security.xml",
        "views/product_view.xml",
        "views/pim_view.xml",
        "views/attribute_set.xml",
        "views/attribute_group.xml",
        "views/attribute_attribute.xml",
    ],
    "demo": [],
    "installable": True,
    "application": True,
}
