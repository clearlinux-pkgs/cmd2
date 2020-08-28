#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmd2
Version  : 1.3.8
Release  : 80
URL      : https://files.pythonhosted.org/packages/42/49/517aac9d1f28391aeb35b3404e06364b67cc0a43f15bafce71ea7a9a62ac/cmd2-1.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/49/517aac9d1f28391aeb35b3404e06364b67cc0a43f15bafce71ea7a9a62ac/cmd2-1.3.8.tar.gz
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
Requires: setuptools
Requires: wcwidth
Requires: which
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : pyperclip
BuildRequires : setuptools
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
Requires: pypi(setuptools)
Requires: pypi(wcwidth)

%description python3
python3 components for the cmd2 package.


%prep
%setup -q -n cmd2-1.3.8
cd %{_builddir}/cmd2-1.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598634929
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
cp %{_builddir}/cmd2-1.3.8/LICENSE %{buildroot}/usr/share/package-licenses/cmd2/034107bef270506011745fc01e2c80493ef9421f
cp %{_builddir}/cmd2-1.3.8/plugins/template/LICENSE %{buildroot}/usr/share/package-licenses/cmd2/3e6eb52ad8a3906e168e16d4a635f441ff29e02b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cmd2/034107bef270506011745fc01e2c80493ef9421f
/usr/share/package-licenses/cmd2/3e6eb52ad8a3906e168e16d4a635f441ff29e02b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
