#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Stem
Summary:	Lingua::Stem - stemming of words
Summary(pl):	Modu³ Perla Lingua::Stem - okre¶laj±cy rdzenie s³ów
Name:		perl-Lingua-Stem
Version:	0.60
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
%if 0%{!?_without_tests:1}
BuildRequires:	perl-Lingua-GL-Stemmer
BuildRequires:	perl-Lingua-Stem-It
BuildRequires:	perl-Lingua-Stem-Snowball-Da
BuildRequires:	perl-Lingua-Stem-Snowball-No
BuildRequires:	perl-Lingua-Stem-Snowball-Se
BuildRequires:	perl-Text-German
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This routine applies stemming algorithms to its parameters, returning
the stemmed words as appropriate to the selected locale.

%description -l pl
Ta funkcja wykonuje na swoich parametrach algorytmy okre¶laj±ce
rdzenie s³ów, zwracaj±c rdzenie s³ów w³a¶ciwe dla ustawionej
lokalizacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
