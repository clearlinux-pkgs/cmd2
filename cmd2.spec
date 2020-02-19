#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmd2
Version  : 0.10.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/d9/de/27517d991bb287e54ad7ea5b20c25ea414c7e08bcd503cc8be959b65a365/cmd2-0.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/de/27517d991bb287e54ad7ea5b20c25ea414c7e08bcd503cc8be959b65a365/cmd2-0.10.1.tar.gz
Summary  : A tool for building interactive command line apps
Group    : Development/Tools
License  : MIT
Requires: cmd2-python = %{version}-%{release}
Requires: cmd2-python3 = %{version}-%{release}
Requires: attrs
Requires: colorama
Requires: pyperclip
Requires: setuptools
Requires: wcwidth
Requires: which
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pyperclip
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : wcwidth
BuildRequires : which

%description
cmd2 is a tool for building interactive command line applications in Python.
Its goal is to make it quick and easy for developers to build feature-rich and
user-friendly interactive command line applications. It provides a simple API
which is an extension of Python's built-in cmd module. cmd2 provides a wealth
of features on top of cmd to make your life easier and eliminates much of the
boilerplate code which would be necessary when using cmd.

%package python
Summary: python components for the cmd2 package.
Group: Default
Requires: cmd2-python3 = %{version}-%{release}

%description python
python components for the cmd2 package.


%package python3
Summary: python3 components for the cmd2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cmd2 package.


%prep
%setup -q -n cmd2-0.10.1
cd %{_builddir}/cmd2-0.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582142027
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
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
