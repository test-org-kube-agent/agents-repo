# GitOps Development & Platform Architecture Guidelines

Welcome to the declarative infrastructure repository for our Google Kubernetes Engine (GKE) platform fleet. This document establishes core engineering standards, directory layouts, and automated remediation boundaries managed by the **Platform Agent**.

---

## 1. Directory Structure

All resources in this repository are managed declaratively under the following directory hierarchy:

```
.
├── README.md                           # Repository entrypoint
├── development-process.md               # This documentation guidelines file
└── clusters/                            # Target cluster configurations
    └── <cluster-name>/                  # Directory per GKE cluster
        ├── gpu-class.yaml               # ComputeClass custom resources
        ├── platform-agent-config.yaml   # Local agent system settings
        └── <application-workloads>.yaml # Individual namespace applications
```

---

## 2. Declarative GitOps Principles

To ensure consistency, security, and traceability, we enforce three hard core truths on our GitOps delivery:

| Principle | Execution Strategy | Verification Mechanism |
| :--- | :--- | :--- |
| **No Manual Mutation** | All manual `kubectl apply/patch/delete` operations are strictly audited and blocked on live cluster resources. | Admission controllers and local OTel audits match states against Git. |
| **Pull-Request Driven** | Every infrastructure or workload alteration must be proposed via a Pull Request against the default branch. | CI/CD testing pipelines run validation tests before human SRE review. |
| **Remediation & Drift Repair** | The **Platform Agent** periodically sweeps configurations, automatically raises PRs to fix drifts, and manages multi-tenant limits. | Event loop reconciliations track remote configurations in active repos. |

---

## 3. Local Cluster Environments

Our fleet consists of the following active GKE environments:

| Cluster Name | Region | Type | Role |
| :--- | :--- | :--- | :--- |
| `platform-agent-host` | `us-east4` | Autopilot | Management Plane & Platform Gateway |
| `c1` | `us-east4` | Standard | High-Performance TPU/GPU Workloads |

---

## 4. Multi-Tenancy Security Baseline

We enforce absolute namespace boundaries on all non-system components:

### 4.1 Network Isolation
Every newly provisioned namespace must contain a default-deny ingress `NetworkPolicy` to ensure zero lateral traffic drift across applications:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: custom-application-ns
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

### 4.2 Resource Boundaries
All namespace allocations require dedicated `ResourceQuotas` and `LimitRanges` to prevent resource starvation across tenant boundaries:

*   **Memory Limit**: Maximum memory usage bounds.
*   **CPU Allocation**: Fair CPU scheduling parameters.
*   **Storage Quota**: Local and network volume PVC limitations.
