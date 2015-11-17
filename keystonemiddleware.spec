#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : keystonemiddleware
Version  : 3.0.0
Release  : 23
URL      : http://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-3.0.0.tar.gz
Source0  : http://tarballs.openstack.org/keystonemiddleware/keystonemiddleware-3.0.0.tar.gz
Summary  : Middleware for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: keystonemiddleware-python
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : PyYAML-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : aioeventlet-python
BuildRequires : amqp-python
BuildRequires : anyjson-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking-python
BuildRequires : iso8601-python
BuildRequires : kombu-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oslo.config-python
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.messaging-python
BuildRequires : oslo.middleware-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable-python
BuildRequires : py-python
BuildRequires : pycadf-python
BuildRequires : pycrypto-python
BuildRequires : pyflakes-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-memcached-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : testrepository-python
BuildRequires : testresources-python
BuildRequires : testscenarios-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : trollius-python
BuildRequires : unittest2-python
BuildRequires : virtualenv

%description
Middleware for the OpenStack Identity API (Keystone)
====================================================

%package python
Summary: python components for the keystonemiddleware package.
Group: Default
Requires: Babel-python
Requires: WebOb-python
Requires: oslo.context-python
Requires: oslo.i18n-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: pycadf-python
Requires: python-keystoneclient-python
Requires: requests-python
Requires: six-python

%description python
python components for the keystonemiddleware package.


%prep
%setup -q -n keystonemiddleware-3.0.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
