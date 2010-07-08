Summary:	twill - Web browsing system
Summary(pl.UTF-8):	twill - System przeglądania sieci WWW
Name:		twill
Version:	0.9
Release:	2
Epoch:		1
License:	MIT
Group:		Applications/Networking
Source0:	http://darcs.idyll.org/~t/projects/%{name}-%{version}.tar.gz
# Source0-md5:	c362307616696f4838e9456c42b70fdc
Patch0:		%{name}-setup.patch
URL:		http://twill.idyll.org/
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
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
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{ANNOUNCE-%{version}.txt,ChangeLog,LICENSE.txt,*.html,*.css}
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*
%{_examplesdir}/%{name}-%{version}
