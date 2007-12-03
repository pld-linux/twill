
Summary:	twill - Web browsing system
Summary(pl.UTF-8):twill - System przeglądania sieci WWW
Name:		twill
Version:	0.9b1
Release:	1
License:	MIT
Group:		Applications
Source0:	http://darcs.idyll.org/~t/projects/%{name}-%{version}.tar.gz
# Source0-md5:	58702a05114a9927fd5ad4cd53c3b226
Patch0:		%{name}-setup.patch
URL:		http://twill.idyll.org/
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:  rpm-pythonprov
%pyrequires_eq  python-modules
Requires:	python >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A scripting system for automating Web browsing. Useful for testing Web
pages or grabbing data from password-protected sites automatically.

%description -l pl.UTF-8
Skryptowy system automatyzujący przeglądanie zawartości sieci WWW.
Twill jest przydatny do testowania stron WWW lub automatycznego
pobierania informacji ze stron zabezpieczonych hasłem.

%prep
%setup -q
%patch0

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/ANNOUNCE-%{version}.txt
%doc doc/{ChangeLog,LICENSE.txt,*.html,*.css}
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/*
%{py_sitescriptdir}/*
