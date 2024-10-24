from abc import ABCMeta, abstractmethod
# abstract class representing instance of DB storing prompt templates data
class PrimaryPromptTemplatesDB(metaclass=ABCMeta):
    # abstract method to get prompt template by id
    @abstractmethod
    def get_prompt_template_by_id(self, req_id: str, client_id: str, prompt_id: int) -> str | None:
        pass

