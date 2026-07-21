# Reporting Issues: Bug Reports and Feature Requests for SmartGen Docs

Your feedback is invaluable to the SmartGen Docs project. Reporting issues, whether they are bugs you've encountered or ideas for new features, helps us improve the platform for everyone. This guide will walk you through the process of effectively reporting issues on our GitHub repository, ensuring your feedback is clear, actionable, and can be addressed efficiently.

## 1. Before Reporting an Issue

Before you open a new issue, please take a moment to perform these preliminary checks:

*   **Search Existing Issues**: Go to the [SmartGen Docs GitHub Issues page](https://github.com/bayeziddev/smartGenDocs/issues) and use the search bar to see if a similar bug has already been reported or if a feature request already exists. If it does, you can add your comments, additional information, or express your support.
*   **Check Documentation**: Consult the [SmartGen Docs Guides](../guides/index.md) and [Tutorials](../tutorials/index.md) to ensure that the behavior you're observing isn't a feature or a misunderstanding of how something works.
*   **Update SmartGen Docs**: Ensure you are using the latest version of SmartGen Docs. Bugs are often fixed in newer releases. You can update by running `pip install --upgrade smartgen-docs`.
*   **Isolate the Problem**: Try to reproduce the issue in a minimal project. This helps in pinpointing the exact cause of the problem.

## 2. How to Report a Bug

When reporting a bug, clarity and detail are key. The more information you provide, the faster we can understand and resolve the issue.

1.  **Navigate to GitHub Issues**: Go to the [SmartGen Docs GitHub Issues page](https://github.com/bayeziddev/smartGenDocs/issues).
2.  **Click "New Issue"**: Look for a button labeled "New issue" or a similar prompt.
3.  **Choose a Template**: Select the "Bug report" template if available. This will pre-fill the issue with sections to guide you.
4.  **Fill in the Details**:
    *   **Title**: Provide a concise and descriptive title. Example: `Bug: Search function fails on pages with special characters`.
    *   **Description**: Clearly describe the bug. What is the problem? What were you trying to achieve?
    *   **Steps to Reproduce**: This is crucial. Provide a numbered list of steps that someone else can follow to reliably reproduce the bug. Include any specific files or configurations if necessary.
        ```markdown
        1. Go to '...' (e.g., your project directory)
        2. Run 'smartgen-docs serve'
        3. Navigate to 'http://127.0.0.1:8000/some-page/'
        4. Observe '...' (e.g., the page does not load, an error appears in the console)
        ```
    *   **Expected Behavior**: Describe what you expected to happen when following the steps.
    *   **Actual Behavior**: Describe what actually happened, including any error messages from the console or terminal.
    *   **Environment**: Provide details about your environment:
        *   SmartGen Docs version (`smartgen-docs --version`)
        *   Python version (`python3 --version`)
        *   Operating System (e.g., Windows 10, macOS Ventura, Ubuntu 22.04)
        *   Browser (if applicable, e.g., Chrome 120, Firefox 118)
        *   Relevant `smartgen.yml` configuration snippets.
    *   **Screenshots/Videos (Optional but Recommended)**: Attach screenshots or short video recordings that clearly demonstrate the bug. This can be incredibly helpful.

## 3. How to Submit a Feature Request

If you have an idea for a new feature or an enhancement to an existing one, we'd love to hear it!

1.  **Navigate to GitHub Issues**: Go to the [SmartGen Docs GitHub Issues page](https://github.com/bayeziddev/smartGenDocs/issues).
2.  **Click "New Issue"**: Look for a button labeled "New issue" or a similar prompt.
3.  **Choose a Template**: Select the "Feature request" template if available.
4.  **Fill in the Details**:
    *   **Title**: Provide a concise and descriptive title. Example: `Feature Request: Add support for Mermaid.js diagrams`.
    *   **Is your feature request related to a problem?**: Clearly describe the problem you're trying to solve with this new feature. Example: "As a user, I find it difficult to create complex diagrams directly in Markdown, which forces me to use external tools and embed images."
    *   **Describe the solution you'd like**: Explain how you envision the feature working. Be as specific as possible.
    *   **Describe alternatives you've considered**: Mention any other solutions or workarounds you've thought about or tried.
    *   **Additional context**: Add any other relevant information, such as use cases, mockups, or why this feature would be particularly beneficial.

## 4. What Happens After You Report an Issue?

Once you've submitted an issue:

*   **Review**: A maintainer will review your issue. They may ask for more information or clarification.
*   **Categorization**: The issue will be categorized with appropriate labels (e.g., `bug`, `enhancement`, `good first issue`).
*   **Prioritization**: Issues are prioritized based on severity, impact, and community interest.
*   **Resolution**: The issue will either be assigned to a contributor, discussed further, or closed if it's a duplicate or not actionable.

We appreciate your patience and understanding throughout this process. Your contributions help make SmartGen Docs a better tool for everyone.

## See Also

*   [Contributing to SmartGen Docs](contributing.md)
*   [Discussions and Support](discussions.md)
*   [SmartGen Docs GitHub Repository](https://github.com/bayeziddev/smartGenDocs)
*   [SmartGen Platform](https://www.smartgentools.com) - Explore the broader SmartGen ecosystem.
