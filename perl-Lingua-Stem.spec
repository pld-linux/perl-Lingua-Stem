#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Stem
Summary:	Lingua::Stem Perl module - stemming of words
Summary(pl):	Modu³ Perla Lingua::Stem - okre¶lanie rdzeni s³ów
Name:		perl-Lingua-Stem
Version:	0.81
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94d85dc2fd40db4483e3bff9206d8cad
%if %{with tests}
BuildRequires:	perl-Lingua-GL-Stemmer
BuildRequires:	perl-Lingua-PT-Stemmer
BuildRequires:	perl-Lingua-Stem-Fr >= 0.02
BuildRequires:	perl-Lingua-Stem-It
BuildRequires:	perl-Lingua-Stem-Snowball-Da >= 1.01
BuildRequires:	perl-Lingua-Stem-Snowball-No >= 1.00
BuildRequires:	perl-Lingua-Stem-Snowball-Se >= 1.01
BuildRequires:	perl-Text-German
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man3/*
