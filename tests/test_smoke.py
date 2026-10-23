"""Every module must at least import."""

import importlib
import pkgutil

import taskem_all


def test_every_module_imports() -> None:
    for m in pkgutil.walk_packages(taskem_all.__path__, "taskem_all."):
        importlib.import_module(m.name)
