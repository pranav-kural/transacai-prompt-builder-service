from abc import ABCMeta, abstractmethod
# abstract class representing instance of DB storing records data
class PrimaryRecordsDB(metaclass=ABCMeta):
    # abstract method to get records given request id, client id, from_time and to_time
    @abstractmethod
    def get_records(self, req_id, client_id, from_time, to_time) -> str | None:
        pass
