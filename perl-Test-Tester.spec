#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Tester
Summary:	Test::Tester - Ease testing test modules built with Test::Builder
Summary(pl.UTF-8):	Test::Tester - ułatwianie testowania modułów testowych z Test::Buildera
Name:		perl-Test-Tester
Version:	0.107
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	998a8abe241992faaa3e90f330800840
URL:		http://search.cpan.org/dist/Test-Tester/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you have written a test module based on Test::Builder then
Test::Tester allows you to test it with the minimum of effort.

%description -l pl.UTF-8
Jeśli moduł testowy jest oparty na klasie Test::Builder, to
Test::Tester umożliwia przetestowanie go minimalnym nakładem pracy.

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
%doc CHANGES README TODO
%{perl_vendorlib}/Test/*.pm
%{perl_vendorlib}/Test/Tester
%{_mandir}/man3/*
