#
# Conditional build:
%bcond_with	tests	# perform "make test" (3 tests fail)

%define 	module	feedparser
Summary:	Parse RSS and Atom feeds in Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Name:		python-%{module}
Version:	5.1.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://feedparser.googlecode.com/files/feedparser-%{version}.tar.bz2
# Source0-md5:	6fb6372a1dc2f56d4d79d740b8f49f25
URL:		http://feedparser.org/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%if %{with tests}
cd %{module}
PYTHONPATH=build %{__python} feedparsertest.py
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README
%{py_sitescriptdir}/feedparser.py[co]
%{py_sitescriptdir}/feedparser-*.egg-info
