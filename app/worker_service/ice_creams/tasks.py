from core.tasks import Task

from .reports import FlavorsReport


class GenerateFlavorsReportTask(Task):
    """
    Generates a list of flavors in an excel file.
    """

    task_name = 'generate_flavors_report_task'

    def run(self, *args, **kwargs):
        report = FlavorsReport()
        report.save_as_file()
