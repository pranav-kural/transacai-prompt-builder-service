# TransacAI Prompt Builder Service

This project is the codebase for the Prompt Builder Service (PBS) of the TransacAI project.

## TransacAI

TransacAI project is geared towards generation of enriched summaries and insights of transactional data in real-time or batch using Generative AI and Large Language Models (LLMs). It goes beyond visual and analytical processing of transactional data by generating context-aware and enriched insights in natural language using LLMs. It focuses on delivering human-centric analysis that is easier to understand and act upon, eliminating the need for multiple complex data processing steps to derive insights from raw data

## Prompt Builder Service (PBS)

The Prompt Builder Service (PBS) is one of the core services of TransacAI. This service is responsible for preparing the prompt that will then be used by the Insights Generation Service (IGS) to generate insights from transactional data.

The PBS is a gRPC service that takes in a request with the following information:

-   **`req_id`**: A unique identifier for a request for idempotency, traceability, and debugging.
-   **`client_id`**: A unique identifier for a client.
-   **`prompt_id`**: ID of the prompt template to be used for generating insights. This allows the client to use different templates for different types of insights and data.
-   **`records_source_id`**: ID of the source of the transactional data records. This allows the client to use different sources of transactional data for generating insights, and also helps improve resiliency by allowing the client to use different sources in case one source is down.
-   **`prompt_templates_source_id`**: ID of the source of the prompt templates. This allows the client to use different sources of prompt templates for generating insights, and also helps improve resiliency by allowing the client to use different sources in case one source is down.
-   **`from_time`**: Start time of the transactional data to be used for generating insights.
-   **`to_time`**: End time of the transactional data to be used for generating insights.

The PBS then prepares the prompt by fetching the prompt template from the database, filling in the placeholders in the template with the transactional data, and returning the prompt to the client.

## Prompt Builder Service

You can find the protobuf definition of the service in the `src/rpc/protos/prompt_builder.proto` file.

The service is implemented in the `src/app.py` file.

## Local Development

### Prerequisites

Its recommended to first initialize a virtual environment before installing the dependencies. You can do this by running the following command:

```bash
python3 -m venv .venv
```

You can then activate the virtual environment by running the following command:

```bash
source .venv/bin/activate
```

You can then install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

### Running the Service

Once, you have installed the dependencies, you can run the service using the following command:

```bash
python src/app.py
```

The service will start running on port `50051`.

### Using Docker

You can also run the service using Docker. You can build the Docker image using the following command:

```bash
docker build -t transac-ai-pbs .
```

You can then run the Docker container using the following command:

```bash
docker run --env-file .env -p 50051:50051 transac-ai-pbs
```

## Testing Locally

To test the service locally, you can use [grpcurl](https://github.com/fullstorydev/grpcurl) to send requests to the service.

```bash
grpcurl -plaintext -d '{"req_id":"1","client_id":"test_client","prompt_id":1,"records_source_id":"SUPABASE","prompt_templates_source_id":"SUPABASE","from_time":"2019-12-29T06:39:22","to_time":"2019-12-29T23:49:22"}' 35.227.31.209:80 prompt_builder.PromptBuilder/BuildPrompt
```

## gRPC

The PBS services exposes a gRPC service. The protobuf definition of the service can be found in the `src/rpc/protos/prompt_builder.proto` file.

Primary service endpoint that is supports is the `BuildPrompt` method.

```protobuf
service PromptBuilder {
  rpc BuildPrompt (BuildPromptRequest) returns (BuildPromptResponse);
}
```

### Regenerating gRPC Code

From `src` directory, run the following command to regenerate the gRPC code:

```bash
sh ./rpc/scripts/gen_prompt_builder_protos.sh
```

This will regenerate the gRPC code in the `src/rpc/protos` directory.

## Deployment (Google Kubernetes Engine)

PBS is deployed on the Google Kubernetes Engine (GKE) in the same cluster as the Insights Generation Service (IGS) to enable efficient low-latency communication between the services.

Manifests for the deployment and service are located in the `kubernetes` directory.

Deployment instructions and information is available in the `kubernetes/README.md` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Issues

If you encounter any issues or bugs while using this project, please report them by following these steps:

1. Check if the issue has already been reported by searching our [issue tracker](https://github.com/transac-ai/transacai-prompt-builder-service/issues).
2. If the issue hasn't been reported, create a new issue and provide a detailed description of the problem.
3. Include steps to reproduce the issue and any relevant error messages or screenshots.

[Open Issue](https://github.com/transac-ai/transacai-prompt-builder-service/issues/new)
