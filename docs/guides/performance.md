# Performance Optimization Guide

SmartGen Docs is engineered for extreme performance, sub-second page compilation, and zero client-side runtime bloat [1]. This guide explores best practices for maintaining high performance across large documentation repositories.

## Zero-Dependency Compilation Model

Unlike documentation frameworks that rely on heavy Node.js or Ruby runtimes with hundreds of transitive dependencies, SmartGen Docs compiles Markdown files directly into static HTML via an optimized Python engine [2]. By eliminating client-side hydration, external font CDNs, and JavaScript framework runtimes, the resulting web pages load instantaneously and achieve perfect scores on Core Web Vitals.

## Build-Time Caching and Asset Namespacing

To scale efficiently across hundreds of pages and multiple theme variants, SmartGen Docs employs strict asset namespacing (`site/static/<theme-name>/`) and optimized traversal algorithms [3]. Caching mechanisms in optional modules like Whoosh search and Pillow image processing ensure that asset compilation overhead remains negligible even during extensive CI builds [4].

## References

- [1] SmartGen Performance Benchmarks. [SmartGen Documentation](https://docs.smartgentools.com/docs/architecture.html).
- [2] Python Build Engine. [SmartGen Source Code](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/core.py).
- [3] Theme Asset Namespacing. [SmartGen Theme Engine](https://github.com/bayeziddev/smartGenDocs/blob/main/smartgen_docs/theme_engine.py).
- [4] Optional Feature Dependencies. [SmartGen Pyproject Configuration](https://github.com/bayeziddev/smartGenDocs/blob/main/pyproject.toml).
