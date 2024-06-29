#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pnam	XString
Summary:	XString - Isolated String helpers from B
Summary(pl.UTF-8):	XString - wyizolowane z B klasy pomocnicze do łańcuchów
Name:		perl-XString
Version:	0.005
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AT/ATOOMIC/%{pnam}-%{version}.tar.gz
# Source0-md5:	da5bbefeeb545e5c2eba2c7576c72e39
URL:		https://metacpan.org/dist/XString
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.87
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XString provides the B string helpers in one isolated package.
Right now only cstring and perlstring are available.

%description -l pl.UTF-8
XString dostarcza klasy pomocnicze B do łańcuchów w jedyn,
samodzielnym pakiecie. Obecnie dostępne są tylko cstring i perlstring.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -pr examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/XString.pm
%dir %{perl_vendorarch}/auto/XString
%attr(755,root,root) %{perl_vendorarch}/auto/XString/XString.so
%{_mandir}/man3/XString.3pm*
%{_examplesdir}/%{name}-%{version}
