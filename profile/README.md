# kubex-py

An asynchronous Kubernetes client for Python, and the libraries around it. Everything is
typed with Pydantic v2 and runs on asyncio or trio.

**Documentation:** https://kubex.codemageddon.me/

| Project | What it is |
|---|---|
| [kubex](https://github.com/kubex-py/kubex) | The client: typed resources, watch, logs, exec and port-forward, over httpx or aiohttp. [PyPI](https://pypi.org/project/kubex/) |
| [kubex-core](https://github.com/kubex-py/kubex-core) | Base models and types shared by kubex and the generated model packages. [PyPI](https://pypi.org/project/kubex-core/) |
| k8s-1.32 … k8s-1.38 | Generated models, one repository per Kubernetes version: [1.32](https://github.com/kubex-py/k8s-1.32) · [1.33](https://github.com/kubex-py/k8s-1.33) · [1.34](https://github.com/kubex-py/k8s-1.34) · [1.35](https://github.com/kubex-py/k8s-1.35) · [1.36](https://github.com/kubex-py/k8s-1.36) · [1.37](https://github.com/kubex-py/k8s-1.37) · [1.38](https://github.com/kubex-py/k8s-1.38). Installed as an extra, e.g. `pip install "kubex[k8s-1.35]"` (package `kubex-k8s-1-35`) |
| [kubex-codegen](https://github.com/kubex-py/kubex-codegen) | The generator for those models, from the Kubernetes OpenAPI spec |
| kubex-runtime | Watchers, reflectors, controllers and finalizers for building operators. In development, not on PyPI yet |
| [pydantic-jsonpointer](https://github.com/kubex-py/pydantic-jsonpointer) | JSON Pointer (RFC 6901) for Pydantic models, dicts and lists |
| [pydantic-jsonpatch](https://github.com/kubex-py/pydantic-jsonpatch) | JSON Patch (RFC 6902) for Pydantic |

```bash
pip install "kubex[httpx,k8s-1.35]"
```

Contributions are welcome: see the [contributing guide](https://github.com/kubex-py/.github/blob/main/CONTRIBUTING.md)
and the [code of conduct](https://github.com/kubex-py/.github/blob/main/CODE_OF_CONDUCT.md). To report a
vulnerability, follow the [security policy](https://github.com/kubex-py/.github/blob/main/SECURITY.md).
