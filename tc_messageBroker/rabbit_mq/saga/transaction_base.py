from typing import Any


class ITransaction:
    def __init__(
        self, queue: str, event: str, order: int, status: str, **kwargs
    ) -> None:
        """
        the transaction happening inside the saga architecture

        Parameters:
        ------------
        queue : str
            what queue the transaction belongs to
        event : str
            the event that transaction belongs to
        order : int
            the order of the transaction in the choreography
        status : int
            the state of the transaction
        **kwargs : dict
            message : any
                the message for the transaction to hold
            start : datetime
                the start time of the transaction
                Can be `None` at the initialization
            end : datetime
                the end time of the transaction
                Can be `None` at the initialization
            runtime : float
                the runtime of the transaction
                Can be `None` at the initialization
            error : Exception
                the error the transaction could encounter
                Can be `None` at the initialization
        """
        self.message = self._get_kwarg("message", kwargs)
        self.start = self._get_kwarg("start", kwargs)
        self.end = self._get_kwarg("end", kwargs)
        self.runtime = self._get_kwarg("runtime", kwargs)
        self.error = self._get_kwarg("error", kwargs)

        self.queue = queue
        self.event = event
        self.order = order
        self.status = status

    def _get_kwarg(self, key: str, kwargs: dict[str, Any], default_value=None):
        if key in kwargs.keys():
            return kwargs[key]
        else:
            return default_value
