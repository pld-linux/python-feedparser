#
# Conditional build:
%bcond_with	tests	# perform "make test" (3 tests fail)

%define 	module	feedparser
Summary:	Feed Parser package for Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Name:		python-%{module}
Version:	5.1.2
Release:	1
License:	PSF
Group:		Libraries/Python
Source0:	http://feedparser.googlecode.com/files/feedparser-%{version}.tar.bz2
# Source0-md5:	9f88692c7c1af1d47839eb2025984975
URL:		http://feedparser.org/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides means for parsing RSS and Atom feeds in Python.

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
%doc README
%{py_sitescriptdir}/feedparser.py[co]
%{py_sitescriptdir}/feedparser-*.egg-info
