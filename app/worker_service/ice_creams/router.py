from app import router

from .tasks import GenerateFlavorsReportTask


router.register(GenerateFlavorsReportTask)
