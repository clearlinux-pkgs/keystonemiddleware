#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x4F398DEAE440091C (infra-root@openstack.org)
#
Name     : keystonemiddleware
Version  : 9.0.0
Release  : 61
URL      : http://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-9.0.0.tar.gz
Source0  : http://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-9.0.0.tar.gz
Source1  : http://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-9.0.0.tar.gz.asc
Summary  : Middleware for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystonemiddleware-license = %{version}-%{release}
Requires: keystonemiddleware-python = %{version}-%{release}
Requires: keystonemiddleware-python3 = %{version}-%{release}
Requires: WebOb
Requires: keystoneauth1
Requires: oslo.cache
Requires: oslo.config
Requires: oslo.context
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: pycadf
Requires: python-keystoneclient
Requires: requests
Requires: six
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : keystoneauth1
BuildRequires : oslo.cache
BuildRequires : oslo.config
BuildRequires : oslo.context
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : pycadf
BuildRequires : python-keystoneclient
BuildRequires : requests
BuildRequires : six

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/keystonemiddleware.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the keystonemiddleware package.
Group: Default

%description license
license components for the keystonemiddleware package.


%package python
Summary: python components for the keystonemiddleware package.
Group: Default
Requires: keystonemiddleware-python3 = %{version}-%{release}

%description python
python components for the keystonemiddleware package.


%package python3
Summary: python3 components for the keystonemiddleware package.
Group: Default
Requires: python3-core
Provides: pypi(keystonemiddleware)
Requires: pypi(oslo.cache)
Requires: pypi(six)
Requires: pypi(oslo.serialization)
Requires: pypi(python_keystoneclient)
Requires: pypi(oslo.i18n)
Requires: pypi(pbr)
Requires: pypi(pycadf)
Requires: pypi(oslo.log)
Requires: pypi(keystoneauth1)
Requires: pypi(oslo.config)
Requires: pypi(webob)
Requires: pypi(requests)
Requires: pypi(oslo.context)
Requires: pypi(oslo.utils)

%description python3
python3 components for the keystonemiddleware package.


%prep
%setup -q -n keystonemiddleware-9.0.0
cd %{_builddir}/keystonemiddleware-9.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585928040
# -Werror is for werrorists
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keystonemiddleware
cp %{_builddir}/keystonemiddleware-9.0.0/LICENSE %{buildroot}/usr/share/package-licenses/keystonemiddleware/9834508b6aa6463fa2da734542dca50f6707c45b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keystonemiddleware/9834508b6aa6463fa2da734542dca50f6707c45b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
