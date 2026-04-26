# Publishing to PyPI

Publishing is automated via GitHub Actions (`.github/workflows/publish.yml`), triggered when a GitHub Release is published.

## Prerequisites

In **GitHub → Settings → Environments**, create an environment named `pypi` and add a secret `PYPI_API_TOKEN` with your PyPI API token.

## Steps

**1. Bump the version** in `pyproject.toml`:

```toml
[project]
version = "0.2.0"
```

**2. Commit and push** to the main branch.

**3. Create a GitHub Release:**
- Go to **GitHub → Releases → Draft a new release**
- Create a tag matching the version (e.g. `v0.2.0`)
- Click **Publish release**

The workflow will build the package and publish it to PyPI automatically.

## Verify

```bash
pip install stt-qubo-core==<version>
```
