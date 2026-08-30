
from hermes_tools import tool_call

def delete_policy(project_id, cluster_name, location):
    tool_call(
        name="mcp__gke__delete_k8s_resource",
        arguments={
            "parent": f"projects/{project_id}/locations/{location}/clusters/{cluster_name}",
            "resourceType": "networkpolicy",
            "name": "baseline-tenant-policy",
            "namespace": "default",
        },
    )

if __name__ == "__main__":
    delete_policy("sergiuspiridon-gkedemos", "platform-agent-host", "us-east4")
    delete_policy("sergiuspiridon-gkedemos", "my-first-cluster", "us-central1")
