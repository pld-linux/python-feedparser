Summary:	Feed Parser package for Python
Summary(pl):	Biblioteka Feed Parser dla Pythona
Name:		python-feedparser
Version:	3.3
Release:	1
License:	Python Software Foundation License
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/feedparser/feedparser-%{version}.zip
# Source0-md5:	f95db0d0e8832197c40a90f517546e21
URL:		http://feedparser.org/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides means for parsing RSS and Atom feeds in Python.

%description -l pl
Ten pakiet umo¿liwia parsowanie ¼róde³ RSS i Atom w Pythonie.

%prep
%setup -qn feedparser

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir} -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/*
