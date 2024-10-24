from core.prompt_builder import build_prompt
from logger.logger import get_testing_logger
from logger.utils import log_error, log_info
from records.records_db_types import RecordsDBType

def run_build_prompt_test():
    try:
      prompt = build_prompt(
          req_id="req_1", 
          client_id="test_client", 
          prompt_id=1, 
          source_id=RecordsDBType.IN_MEMORY,
          from_time="2019-12-29T06:39:22", 
          to_time="2019-12-29T23:49:22"
          )
      assert prompt is not None
    except Exception as e:
      get_testing_logger().info(f"Test - run_build_prompt_test - Failed with error: {str(e)}")
    
    get_testing_logger().info("Test - run_build_prompt_test - Passed")

def run_build_prompt_invalid_prompt_id_test():
    try:
      build_prompt(
          req_id="req_1", 
          client_id="test_client", 
          prompt_id=100, 
          source_id=RecordsDBType.IN_MEMORY,
          from_time="2019-12-29T06:39:22", 
          to_time="2019-12-29T23:49:22"
          )
      
      get_testing_logger().info("Test - run_build_prompt_invalid_prompt_id_test - Failed")
    except Exception as e:
      get_testing_logger().info(f"Test - run_build_prompt_invalid_prompt_id_test - Passed with error: {str(e)}")

def run_build_prompt_invalid_records_test():
    try:
      build_prompt(
          req_id="req_1", 
          client_id="test_client", 
          prompt_id=1, 
          source_id=RecordsDBType.IN_MEMORY,
          from_time="2019-12-29T06:49:22", 
          to_time="2019-12-29T06:49:22"
          )
      
      get_testing_logger().info("Test - run_build_prompt_invalid_records_test - Failed")
    except Exception as e:
      get_testing_logger().info(f"Test - run_build_prompt_invalid_records_test - Passed with error: {str(e)}")