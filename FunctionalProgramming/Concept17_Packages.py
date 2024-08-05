"""
Packages are nothing but a group of related modules
Packages can contain sub-packages in them as well
Packages help us to resolve naming conflicts
Before Python 3.3 a folder can be treated as a Python package if it contains __init__.py file
Since Python 3.3 we don't need to have __init__.py file inside a folder to be considered as a package
"""

# The below code is a perfect example to demonstrate how packages help us to resolve naming conflicts
import UserDefinedPackages.com.module1 as cm1
from UserDefinedPackages.com.package1.module1 import f1
import UserDefinedPackages.package2.module1

f1()
cm1.f1()
UserDefinedPackages.package2.module1.f1()
