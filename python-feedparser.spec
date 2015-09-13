#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
%bcond_with	tests	# perform "make test" (3 tests fail)

%define 	module	feedparser
Summary:	Parse RSS and Atom feeds in Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Name:		python-%{module}
Version:	5.1.3
Release:	3
License:	BSD
Group:		Libraries/Python
Source0:	http://feedparser.googlecode.com/files/feedparser-%{version}.tar.bz2
# Source0-md5:	6fb6372a1dc2f56d4d79d740b8f49f25
URL:		http://feedparser.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Universal Feed Parser is a Python module for downloading and parsing
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, Userland
RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, Atom 0.3,
Atom 1.0, and CDF feeds. It also parses several popular extension
modules, including Dublin Core and Apple's iTunes extensions.

%description -l pl.UTF-8
Ten pakiet umożliwia analizę źródeł RSS i Atom w Pythonie.

%package -n python3-%{module}
Summary:	Parse RSS and Atom feeds in Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Universal Feed Parser is a Python module for downloading and parsing
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, Userland
RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, Atom 0.3,
Atom 1.0, and CDF feeds. It also parses several popular extension
modules, including Dublin Core and Apple's iTunes extensions.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet umożliwia analizę źródeł RSS i Atom w Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build

%if %{with python2}
%{__python} setup.py build --build-base build-2
%{?with_tests:cd feedparser; PYTHONPATH=../build-2 %{__python} feedparsertest.py; cd ..}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3
%{?with_tests:cd feedparser; PYTHONPATH=../build-3 %{__python} feedparsertest.py; cd ..}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
        build --build-base build-2 \
        install --skip-build \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
        build --build-base build-3 \
        install --skip-build \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/feedparser.py[co]
%{py_sitescriptdir}/feedparser-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py3_sitescriptdir}/feedparser.py
%{py3_sitescriptdir}/__pycache__/feedparser.*.py[co]
%{py3_sitescriptdir}/feedparser-*.egg-info
%endif
