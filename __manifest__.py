{
    'name': "hms patient",
    'depends': ['base', 'crm'],
    "data": [
        "security/security.xml",
        "wizard/wizard_example_view.xml",
        "security/ir.model.access.csv",
        "views/hms_patient_view.xml",
        "views/hms_department_view.xml",
        "views/hms_doctors_view.xml",
        "views/crm_inherited_view.xml",
        "reports/report.xml",
        "reports/hms_templates.xml",
        "reports/report_wizard.xml",
        "reports/wizard_template.xml"
    ]
}
