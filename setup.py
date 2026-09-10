from setuptools import find_packages, setup


DEPENDENCIES = [
	"dash",
	"flask-compress",
	"numpy",
	"plotly",
]


setup(
	name = "profile-dashboard",
	version = "0.0.1",
	description = "Dashboard to visualize live or file-based data",
	author = "Andrii Pastushenko",
	url = "https://github.com/drozzoff/dashboard",
	python_requires =">=3.10",
	license = "MIT", 

	packages = find_packages(include = ["dashboard", "dashboard.*"]),
	package_data = {
		"dashboard": [
			"assets/*.css",
			"assets/*.js",
		],
	},
	install_requires = DEPENDENCIES,
)