import importlib
import pkgutil

import dashboard

module_names = [
	module.name
	for module in pkgutil.walk_packages(dashboard.__path__, prefix = f"{dashboard.__name__}.")
]

for module_name in module_names:
	importlib.import_module(module_name)
	print(f"Imported {module_name}")

print(f"Successfully imported dashboard and {len(module_names)} core submodules")