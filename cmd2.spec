#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmd2
Version  : 2.1.0
Release  : 94
URL      : https://files.pythonhosted.org/packages/15/7d/7b7a1ef794ea3d7176387f73af9e475f8ccc3b1991fc29d7ddb63174ce07/cmd2-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/15/7d/7b7a1ef794ea3d7176387f73af9e475f8ccc3b1991fc29d7ddb63174ce07/cmd2-2.1.0.tar.gz
Summary  : A tool for building interactive command line apps
Group    : Development/Tools
License  : MIT
Requires: cmd2-license = %{version}-%{release}
Requires: cmd2-python = %{version}-%{release}
Requires: cmd2-python3 = %{version}-%{release}
Requires: attrs
Requires: colorama
Requires: importlib_metadata
Requires: pyperclip
Requires: typing_extensions
Requires: wcwidth
Requires: which
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : pyperclip
BuildRequires : setuptools_scm
BuildRequires : wcwidth
BuildRequires : which

%description
cmd2 is a tool for building interactive command line applications in Python.
Its goal is to make it quick and easy for developers to build feature-rich and
user-friendly interactive command line applications. It provides a simple API
which is an extension of Python's built-in cmd module. cmd2 provides a wealth
of features on top of cmd to make your life easier and eliminates much of the
boilerplate code which would be necessary when using cmd.

%package license
Summary: license components for the cmd2 package.
Group: Default

%description license
license components for the cmd2 package.


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
Provides: pypi(cmd2)
Requires: pypi(attrs)
Requires: pypi(colorama)
Requires: pypi(pyperclip)
Requires: pypi(wcwidth)

%description python3
python3 components for the cmd2 package.


%prep
%setup -q -n cmd2-2.1.0
cd %{_builddir}/cmd2-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623710144
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cmd2
cp %{_builddir}/cmd2-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/cmd2/034107bef270506011745fc01e2c80493ef9421f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cmd2/034107bef270506011745fc01e2c80493ef9421f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
