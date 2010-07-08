Summary:	Feed Parser package for Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Name:		python-feedparser
Version:	4.1
Release:	4
License:	Python Software Foundation License
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/feedparser/feedparser-%{version}.zip
# Source0-md5:	7ab1140c1e29d4cd52ab20fa7b1f8640
URL:		http://feedparser.org/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides means for parsing RSS and Atom feeds in Python.

%description -l pl.UTF-8
Ten pakiet umożliwia analizę źródeł RSS i Atom w Pythonie.

%prep
%setup -qc

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*
