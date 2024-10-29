# Deploying PBS to Google Kubernetes Engine (GKE)

This guide provides instructions for deploying the PBS service to Google Kubernetes Engine (GKE).

## Steps

1. Confirm project.

```bash
gcloud config get-value project
```

2. Create the `pbs-repo` repository in Artifact Registry.

```bash
gcloud artifacts repositories create pbs-repo \
    --project=transac-ai \
    --repository-format=docker \
    --location=us-east1 \
    --description="Transac AI Prompt Builder Service (PBS) Repository"
```

3. Build the `pbs-gke` container image using [Cloud Build](https://cloud.google.com/build).

```bash
gcloud builds submit --tag us-east1-docker.pkg.dev/transac-ai/pbs-repo/transac-ai-pbs-gke .
```

4. Create `transac-ai-gke` GKE cluster is not already created.

```bash
gcloud container clusters create-auto transac-ai-gke --location us-east1
```

5. Set secrets for environment variables.

```
kubectl create secret generic transac-ai-pbs-secrets \
--from-literal=transac-ai-pbs-log-mode='' \
--from-literal=transac-ai-pbs-supabase-url='' \
--from-literal=transac-ai-pbs-supabase-key='' \
--from-literal=transac-ai-pbs-server-port=''
```

6. The deployment Kubernetes manifest is located at `kubernetes/deployment.yaml`. Apply the manifest to the GKE cluster.

```bash
kubectl apply -f kubernetes/deployment.yaml
```

7. You can use the below commands to check status of the deployment, service, and pods.

```bash
kubectl get deployments
kubectl get pods
```

8. There is also a `service.yaml` manifest that defines a Load Balancer service for the deployment for it to be accessible externally through TCP. Apply the manifest to the GKE cluster.

```bash
kubectl apply -f kubernetes/service.yaml
```

9. To access the service, you can use the Load Balancer IP address.

```bash
kubectl get services
```

The external IP address is listed under the column `EXTERNAL-IP` for the `transac-ai-pbs-service` Service.

Output:

```bash
NAME                     TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)        AGE
transac-ai-pbs-service   LoadBalancer   **.***.***.***   **.***.***.***    80:31645/TCP   3h47m
```

10. You can now access and test the service using the external IP address.

Replace `<EXTERNAL-IP>` with the actual external IP address in the below command.

```bash
grpcurl -plaintext \
-d '{"req_id":"1","client_id":"test_client","prompt_id":1,"records_source_id":"SUPABASE","prompt_templates_source_id":"SUPABASE","from_time":"2019-12-29T06:39:22","to_time":"2019-12-29T23:49:22"}' \
<EXTERNAL-IP>:80 prompt_builder.PromptBuilder/BuildPrompt
```
