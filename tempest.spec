#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tempest
Version  : 19.0.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/fb/c7/43a6b75c69bc620299e18391dc752c7bb9b0db77ca0b76235e2d506362ea/tempest-19.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fb/c7/43a6b75c69bc620299e18391dc752c7bb9b0db77ca0b76235e2d506362ea/tempest-19.0.0.tar.gz
Summary  : OpenStack Integration Testing
Group    : Development/Tools
License  : Apache-2.0
Requires: tempest-bin = %{version}-%{release}
Requires: tempest-data = %{version}-%{release}
Requires: tempest-license = %{version}-%{release}
Requires: tempest-python = %{version}-%{release}
Requires: tempest-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cliff
Requires: debtcollector
Requires: fixtures
Requires: jsonschema
Requires: netaddr
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: paramiko
Requires: pbr
Requires: python-subunit
Requires: six
Requires: stestr
Requires: stevedore
Requires: testtools
Requires: unittest2
Requires: urllib3
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : coverage-python
BuildRequires : debtcollector
BuildRequires : fixtures
BuildRequires : flake8-import-order-python
BuildRequires : hacking
BuildRequires : jsonschema
BuildRequires : jsonschema-python
BuildRequires : netaddr
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.log
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslotest
BuildRequires : oslotest-python
BuildRequires : paramiko
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-subunit
BuildRequires : six
BuildRequires : stestr
BuildRequires : stevedore
BuildRequires : testtools
BuildRequires : tox
BuildRequires : unittest2
BuildRequires : urllib3
BuildRequires : virtualenv
Patch1: deps.patch

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the tempest package.
Group: Binaries
Requires: tempest-data = %{version}-%{release}
Requires: tempest-license = %{version}-%{release}

%description bin
bin components for the tempest package.


%package data
Summary: data components for the tempest package.
Group: Data

%description data
data components for the tempest package.


%package license
Summary: license components for the tempest package.
Group: Default

%description license
license components for the tempest package.


%package python
Summary: python components for the tempest package.
Group: Default
Requires: tempest-python3 = %{version}-%{release}

%description python
python components for the tempest package.


%package python3
Summary: python3 components for the tempest package.
Group: Default
Requires: python3-core
Provides: pypi(tempest)
Requires: pypi(cliff)
Requires: pypi(debtcollector)
Requires: pypi(fixtures)
Requires: pypi(jsonschema)
Requires: pypi(netaddr)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.log)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(paramiko)
Requires: pypi(pbr)
Requires: pypi(prettytable)
Requires: pypi(python_subunit)
Requires: pypi(pyyaml)
Requires: pypi(six)
Requires: pypi(stestr)
Requires: pypi(stevedore)
Requires: pypi(testtools)
Requires: pypi(unittest2)
Requires: pypi(urllib3)

%description python3
python3 components for the tempest package.


%prep
%setup -q -n tempest-19.0.0
cd %{_builddir}/tempest-19.0.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583717127
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tempest
cp %{_builddir}/tempest-19.0.0/LICENSE %{buildroot}/usr/share/package-licenses/tempest/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/skip-tracker
rm -f %{buildroot}/usr/bin/check-uuid
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc
mv %{buildroot}/usr/etc/tempest %{buildroot}/usr/share/defaults/etc/
rm -rf %{buildroot}/usr/etc
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/subunit-describe-calls
/usr/bin/tempest
/usr/bin/tempest-account-generator
/usr/bin/verify-tempest-config

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/tempest/accounts.yaml.sample
/usr/share/defaults/etc/tempest/logging.conf.sample
/usr/share/defaults/etc/tempest/whitelist.yaml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tempest/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
