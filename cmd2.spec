#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmd2
Version  : 0.6.9
Release  : 20
URL      : http://pypi.debian.net/cmd2/cmd2-0.6.9.tar.gz
Source0  : http://pypi.debian.net/cmd2/cmd2-0.6.9.tar.gz
Summary  : Extra features for standard library's cmd module
Group    : Development/Tools
License  : MIT
Requires: cmd2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyparsing
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
----
cmd2
----
.. image:: https://secure.travis-ci.org/python-cmd2/cmd2.png?branch=master
:target: http://travis-ci.org/python-cmd2/cmd2
:alt: Build status

%package python
Summary: python components for the cmd2 package.
Group: Default

%description python
python components for the cmd2 package.


%prep
%setup -q -n cmd2-0.6.9

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484539302
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484539302
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
