# API Reference Overview

Welcome to the **API Reference** section of SmartGen Docs. This comprehensive guide is intended for developers who want to interact programmatically with the SmartGen Docs platform or extend its functionality.

While SmartGen Docs is primarily a static site generator driven by Markdown and YAML configuration, it also provides internal APIs and tools (like the `autodoc` feature) that can be leveraged for advanced use cases, automation, and integration with other systems.

## In This Section

This section covers the following key areas:

*   **[Authentication](authentication.md)**: Learn how to authenticate your requests if you are interacting with any secured endpoints or the Upload Manager.
*   **[REST API](rest-api.md)**: Understand the general principles, conventions, and structure of the SmartGen Docs REST API (if applicable to your deployment).
*   **[Endpoints](endpoints.md)**: Detailed documentation of available API endpoints, including request parameters, response formats, and examples.
*   **[Error Codes](errors.md)**: A comprehensive list of potential error codes returned by the API, along with explanations and troubleshooting steps.
*   **[Rate Limits](rate-limits.md)**: Information on API rate limiting policies to ensure fair usage and system stability.
*   **[Webhooks](webhooks.md)**: Learn how to configure and use webhooks to receive real-time notifications about events within your SmartGen Docs project.

## Getting Started with the API

If you are new to the SmartGen Docs API, we recommend starting with the **[Authentication](authentication.md)** and **[REST API](rest-api.md)** pages to understand the basic requirements and conventions.

For generating API documentation for your own Python projects using SmartGen Docs, refer to the `autodoc` feature described in the [Features](../docs/features.md) section and the CLI documentation.

## SDKs and Client Libraries

To simplify integration, we provide SDKs for several popular programming languages. These libraries handle authentication, request formatting, and response parsing, allowing you to focus on your application logic.

Explore the available SDKs in the **[SDKs Section](../sdk/index.md)**.
