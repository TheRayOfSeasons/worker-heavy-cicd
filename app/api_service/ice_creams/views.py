from core.views import DelegatedWorkerView

from services import Services


class FlavorsReportView(DelegatedWorkerView):
    """
    Sends a payload to the worker service
    to generate a flavors report.
    """

    task_name = 'generate_flavors_report_task'
