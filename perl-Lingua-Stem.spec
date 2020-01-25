#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Lingua
%define		pnam	Stem
Summary:	Lingua::Stem Perl module - stemming of words
Summary(pl.UTF-8):	Moduł Perla Lingua::Stem - określanie rdzeni słów
Name:		perl-Lingua-Stem
Version:	0.84
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a236b5d85ac49f84aad447c1383ad2de
URL:		http://search.cpan.org/dist/Lingua-Stem/
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

%description -l pl.UTF-8
Ta funkcja wykonuje na swoich parametrach algorytmy określające
rdzenie słów, zwracając rdzenie słów właściwe dla ustawionej
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
%{perl_vendorlib}/Lingua/*.pm
%{perl_vendorlib}/Lingua/Stem/*.pm
%{_mandir}/man3/*
