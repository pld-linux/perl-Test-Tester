# NOTE: now part of perl-Test-Simple
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Test
%define	pnam	Tester
Summary:	Test::Tester - Ease testing test modules built with Test::Builder
Summary(pl.UTF-8):	Test::Tester - ułatwianie testowania modułów testowych z Test::Buildera
Name:		perl-Test-Tester
Version:	0.109
Release:	1.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8fd872ee7e959f89a4af0371a7e782d
URL:		http://search.cpan.org/dist/Test-Tester/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%{perl_vendorlib}/Test/Tester.pm
%{perl_vendorlib}/Test/Tester
%{_mandir}/man3/Test::Tester*.3pm*
