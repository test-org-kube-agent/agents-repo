# test-org-kube-agent Agents Repository

Welcome to the central platform administration and GitOps configuration repository for `test-org-kube-agent`.

## Project Overview

This repository acts as the single source of truth for our declarative GKE infrastructure lifecycle, access boundaries, security policy settings, and automated agent configurations across the fleet.

## Fleet Structure

Our fleet comprises the following key infrastructure environments:

1. **Management Cluster (`platform-agent-host`)**: Deployed in `us-east4`, hosting the central control plane, the Platform Agent Gateway, and related system components (such as GitHub Token Minter and OTel metrics collector).
2. **Managed Clusters**: Remote runtime environments that host SRE workloads and single-cluster SRE agents (such as Cluster Agent `c1` in `us-central1`).

## Directory Layout

- `/clusters`: Contains declarative GKE cluster specifications and environmental configurations.
- `README.md`: Central documentation and onboarding guidelines.

## Declarative Workflow (GitOps)

Infrastructure and platform updates are proposed via automated Pull Requests rather than manual direct modifications. Every proposed change undergoes peer review and must be approved by SRE before merging.
