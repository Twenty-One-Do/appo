import importlib
import logging
import os
from types import ModuleType

from fastapi import APIRouter, FastAPI

from appo_api.config import settings

log = logging.getLogger(__name__)


def import_db_models() -> None:
    import_modules("app", "models")


def add_routers(app: FastAPI, package_names: list[str]) -> None:
    modules = []
    for package_name in package_names:
        modules.extend(import_modules(package_name, "router"))

    for module in modules:
        if "router" not in dir(module):
            continue

        router = module.router
        if not isinstance(router, APIRouter):
            log.warning(f"router: '{router}' is not APIRouter instance")
            continue

        app.include_router(router)


def import_modules(package: str, namespace: str, domains: list[str] | None = None) -> list[ModuleType]:
    # 지정한 패키지 디렉터리 경로로 변환
    packages = package.split(".")
    package_path = os.path.join(settings.BASE_DIR, *packages)

    module_names = []
    for rootdir, _, files in os.walk(package_path):
        # 해당하는 패키지 내 모듈 추가
        if os.path.basename(rootdir) == namespace:
            for filename in files:
                file_path = os.path.join(rootdir, filename)
                module_names.append(_path_to_modulename(settings.ROOT_DIR, file_path))
            continue

        # 모듈이 존재하는 경우 해당 모듈 추가
        for filename in files:
            file_path = os.path.join(rootdir, filename)
            if filename == f"{namespace}.py":
                module_names.append(_path_to_modulename(settings.ROOT_DIR, file_path))

    modules = []
    for module_name in module_names:
        modules.append(importlib.import_module(module_name))

    return modules


def _path_to_modulename(base_path: str, module_path: str) -> str:
    rel_path = os.path.relpath(module_path, base_path)
    if rel_path.endswith(".py"):
        rel_path = rel_path[:-3]

    module_name = rel_path.replace(os.path.sep, ".")
    return module_name
