%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Stem
Summary:	Lingua::Stem -- Stemming of words
Summary(pl):	Modu³ Perla Lingua::Stem - okre¶laj±cy temat s³ów
Name:		perl-%{pdir}-%{pnam}
Version:	0.50
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This routine applies stemming algorithms to its parameters, returning
the stemmed words as appropriate to the selected locale.

%description -l pl
Ta funkcja wykonuje na swoich parametrach algorytmy okre¶laj±ce temat
s³owa, zwracaj±c tematy s³ów w³a¶ciwe dla ustawionej lokalizacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
