# SDKs Overview

Welcome to the **SDKs (Software Development Kits)** section of SmartGen Docs. This section is dedicated to providing resources and client libraries that simplify programmatic interaction with the SmartGen Docs platform and its underlying services. SDKs abstract away the complexities of direct API calls, allowing developers to integrate SmartGen Docs functionalities into their applications more efficiently.

## What are SDKs?

An SDK is a collection of software development tools in one installable package. They are language-specific and typically include:

*   **Client Libraries**: Pre-built code (e.g., Python classes, JavaScript functions) that wrap API endpoints, making them easier to call.
*   **Documentation**: Guides and examples on how to use the SDK.
*   **Tools**: Utilities for authentication, data serialization/deserialization, and error handling.
*   **Code Samples**: Ready-to-use snippets to accelerate development.

## Why Use an SDK?

Using an SDK offers several advantages over making raw HTTP requests to the API:

*   **Simplified Development**: Reduces boilerplate code and handles common tasks like authentication, request signing, and error parsing.
*   **Increased Productivity**: Speeds up development by providing ready-to-use functions and objects.
*   **Type Safety (in some languages)**: Can provide type hints and auto-completion, reducing errors.
*   **Easier Maintenance**: SDKs are typically maintained by the API provider, ensuring compatibility with API updates.

## Available SDKs (Conceptual)

Currently, SmartGen Docs provides (or plans to provide) SDKs for the following programming languages:

### 1. Python SDK

The Python SDK allows Python developers to easily interact with the SmartGen Docs API. It provides classes and methods for managing documents, triggering builds, and accessing site information.

*   **Installation**: `pip install smartgendocs-sdk-python`
*   **Key Features**:
    *   Document upload and retrieval.
    *   Site build management.
    *   Configuration access.
*   **[Python SDK Reference](python-sdk.md)**: Detailed documentation for the Python client library.

### 2. JavaScript SDK

The JavaScript SDK is designed for web and Node.js developers, enabling seamless integration of SmartGen Docs functionalities into front-end applications or server-side scripts.

*   **Installation**: `npm install smartgendocs-sdk-js` or `yarn add smartgendocs-sdk-js`
*   **Key Features**:
    *   Asynchronous API calls.
    *   Browser and Node.js compatibility.
    *   Event handling for webhooks.
*   **[JavaScript SDK Reference](javascript-sdk.md)**: Detailed documentation for the JavaScript client library.

## Getting Started with an SDK

1.  **Choose Your Language**: Select the SDK that matches your development environment.
2.  **Installation**: Follow the installation instructions for your chosen SDK.
3.  **Authentication**: Configure your API credentials as described in the SDK documentation (refer to [API Authentication](../api/authentication.md)).
4.  **Explore Examples**: Use the provided code examples to quickly get started with common tasks.

## Contributing to SDKs

We welcome contributions to our SDKs. If you find a bug, have a feature request, or would like to contribute code, please refer to the individual SDK repositories on GitHub. Your contributions help us improve the developer experience for everyone.

For general API concepts, refer to the [API Reference Overview](../api/index.md).
