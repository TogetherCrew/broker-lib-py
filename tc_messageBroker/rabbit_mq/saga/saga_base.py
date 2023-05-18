from .choreography_base import IChoreography
import uuid
import datetime


class ISaga:
    def __init__(
        self,
        choreography: IChoreography,
        status: str,
        data: any,
        created_at: datetime,
        next: callable = None,
    ) -> None:
        self.uuid = str(uuid.uuid4)
        self.choreography = choreography
        self.status = status
        self.data = data
        created_at = created_at
        self.next = next
