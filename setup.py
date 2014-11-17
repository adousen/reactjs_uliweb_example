import uliweb
from uliweb.utils.setup import setup
import apps

__doc__ = """doc"""

setup(name='comment',
    version=apps.__version__,
    description="Description of your project",
    package_dir = {'comment':'apps'},
    packages = ['comment'],
    include_package_data=True,
    zip_safe=False,
)
