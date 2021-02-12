from django.views.generic import TemplateView

from braces.views import JSONResponseMixin

from services import Services


class JSONView(JSONResponseMixin, TemplateView):
    """
    A view dedicated for responding customized json data.

    Reference:
    https://docs.djangoproject.com/en/3.0/topics/class-based-views/mixins/#more-than-just-html
    """

    disable_get = False

    def render_to_response(self, context, **response_kwargs):
        """
        This totally overrides the template view's render_to_response
        method. Rather than responding an html rendered through django
        templates, this will response a json that contains the values
        returned by get_context_data.
        """
        return self.render_json_response(context, **response_kwargs)

    def get(self, request, *args, **kwargs):
        if self.disable_get:
            raise Http404(f'GET is disabled for {self.__class__.__name__}')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Do the same thing with Post.
        """
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class DelegatedWorkerInterface(object):
    """
    An interface mixin for the delegated worker view.
    """

    task_name = ''
    payload_args = []
    payload_kwargs = {}

    def get_task_name(self, *args, **kwargs):
        """
        A virtual method for assembling the value
        of the payload's `task` key, should there
        be a need for any dynamic implementations.
        """
        return self.task_name

    def get_payload_args(self, *args, **kwargs):
        """
        A virtual method for assembling the value
        of the payload's `arg` key.
        """
        return self.payload_args

    def get_payload_kwargs(self, *args, **kwargs):
        """
        A virtual method for assembling the value
        of the payload's `arg` key.
        """
        return self.payload_kwargs


class DelegatedWorkerView(DelegatedWorkerInterface, JSONView):
    """
    Delagates an asyncronous task to the worker service.
    This way, the load of the task won't interfere with
    the performance of the main application in the server.
    """

    # If errors are raised or just returned as an alternative
    # response for the front-end to handle.
    throw_errors = True
    disable_get = True

    def get_error_message(self, error, *args, **kwargs):
        """
        Returns the error message should this be
        configured not to throw errors in the
        backend, and instead let it be handled
        by the front end.
        """
        return {
            'status': 400,
            'raw_error': error,
            'message': 'Invalid arguments.'
        }

    def get_success_message(self, *args, **kwargs):
        """
        Returns the success message.
        """
        return {
            'status': 200,
            'message': (
                'Process successfully delegated '
                'to worker microservice.'
            )
        }

    def _delegate_to_workers(self, *args, **kwargs):
        """
        Sends the delegated values to the worker service.
        """
        try:
            task = self.get_task_name(*args, **kwargs)
            payload_args = self.get_payload_args(*args, **kwargs)
            payload_kwargs = self.get_payload_kwargs(*args, **kwargs)
            Services.Workers.send_payload(
                task,
                *payload_args,
                **payload_kwargs
            )
        except Exception as e:
            if not self.throw_errors:
                return self.get_error_message(e, *args, **kwargs)
            else:
                raise e
        return self.get_success_message()

    def get_context_data(self, *args, **kwargs):
        return self._delegate_to_workers(*args, **kwargs)
