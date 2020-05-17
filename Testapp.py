from __future__ import print_function
import pandas as pd
import numpy as np
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

sales_report ='Themba Pakula'
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "MBSA_BudgetReport ",
                 "national_pivot_table": sales_report}
html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("ITBugetReport.pdf")