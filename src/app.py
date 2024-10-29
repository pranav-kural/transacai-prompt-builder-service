import os
import grpc
from concurrent import futures
from grpc_reflection.v1alpha import reflection
from core.prompt_builder import build_prompt
from logger.utils import log_error
from prompts.prompt_templates_db_types import get_prompt_templates_db_type_from_str
from records.records_db_types import get_records_db_type_from_str
from rpc.protos import prompt_builder_pb2
from rpc.protos import prompt_builder_pb2_grpc
from dotenv import load_dotenv

load_dotenv()

class PromptBuilder(prompt_builder_pb2_grpc.PromptBuilderServicer):
    def BuildPrompt(self, request: prompt_builder_pb2.BuildPromptRequest, context):

        # Identify source
        try:
            records_source_id = get_records_db_type_from_str(request.records_source_id)
        except ValueError as e:
            log_error(f"PromptBuilder - BuildPrompt - Invalid source_id: {request.records_source_id}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return prompt_builder_pb2.BuildPromptResponse()
        
        # Identify prompt template source
        try:
            prompt_templates_source_id = get_prompt_templates_db_type_from_str(request.prompt_templates_source_id)
        except ValueError as e:
            log_error(f"PromptBuilder - BuildPrompt - Invalid prompt_templates_source_id: {request.prompt_templates_source_id}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return prompt_builder_pb2.BuildPromptResponse()

        try:
          # Build the prompt
          prompt = build_prompt(
              req_id=request.req_id,
              client_id=request.client_id,
              prompt_id=request.prompt_id,
              records_source_id=records_source_id,
              prompt_templates_source_id=prompt_templates_source_id,
              from_time=request.from_time,
              to_time=request.to_time,
          )
          # validate prompt
          if prompt is None:
              log_error(f"PromptBuilder - BuildPrompt - Invalid prompt")
              raise Exception("Prompt generation failed - Invalid prompt")
          # Return the prompt
          return prompt_builder_pb2.BuildPromptResponse(prompt=prompt)
        except Exception as e:
          # Log the error
          log_error(f"PromptBuilder - BuildPrompt - Error: {e}")
          # Raise the error
          context.set_details(str(e))
          context.set_code(grpc.StatusCode.INTERNAL)
          return prompt_builder_pb2.BuildPromptResponse()
        
def create_server(server_address: str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prompt_builder_pb2_grpc.add_PromptBuilderServicer_to_server(PromptBuilder(), server)
    SERVICE_NAMES = (
        prompt_builder_pb2.DESCRIPTOR.services_by_name['PromptBuilder'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    port = server.add_insecure_port(server_address)
    return server, port
    

def serve(server):
    server.start()
    server.wait_for_termination()

def main():
    default_port = os.getenv("SERVER_PORT", "50051")
    server, unused_port = create_server(f"[::]:{default_port}")
    serve(server)

if __name__ == "__main__":
    main()