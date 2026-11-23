# kubex-py

An asynchronous Kubernetes client for Python, and the libraries around it. Everything is
typed with Pydantic v2 and runs on asyncio or trio.

**Documentation:** https://kubex.codemageddon.me/

| Project | What it is |
|---|---|
| [kubex](https://github.com/kubex-py/kubex) | The client: typed resources, watch, logs, exec and port-forward, over httpx or aiohttp. [PyPI](https://pypi.org/project/kubex/) |
| [kubex-core](https://pypi.org/project/kubex-core/) | Base models and types shared by kubex and the generated model packages |
| [kubex-k8s-1-32 … 1-38](https://pypi.org/project/kubex-k8s-1-35/) | Generated models for each Kubernetes version, installed as an extra: `pip install "kubex[k8s-1.35]"` |
| kubex-runtime | Watchers, reflectors, controllers and finalizers for building operators. In development, not on PyPI yet |
| [pydantic-jsonpointer](https://github.com/kubex-py/pydantic-jsonpointer) | JSON Pointer (RFC 6901) for Pydantic models, dicts and lists |
| [pydantic-jsonpatch](https://github.com/kubex-py/pydantic-jsonpatch) | JSON Patch (RFC 6902) for Pydantic |
| [showcase](https://github.com/kubex-py/showcase) | An example operator built with kubex and kubex-runtime |

```bash
pip install "kubex[httpx,k8s-1.35]"
```

Contributions are welcome: see the [contributing guide](https://github.com/kubex-py/.github/blob/main/CONTRIBUTING.md)
and the [code of conduct](https://github.com/kubex-py/.github/blob/main/CODE_OF_CONDUCT.md). To report a
vulnerability, follow the [security policy](https://github.com/kubex-py/.github/blob/main/SECURITY.md).
