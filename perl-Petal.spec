%define module   Petal

Name:		perl-%{module}
Version:	2.20
Release:	2
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl Template Attribute Language
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(MKDoc::XML)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(CGI)
BuildArch:	noarch

%description
Examples deal with using Petal to generate HTML files from HTML templates.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Petal.pm
%{perl_vendorlib}/Petal

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.19-3mdv2010.0
+ Revision: 430525
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.19-2mdv2009.0
+ Revision: 268712
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.19-1mdv2009.0
+ Revision: 213670
- import perl-Petal


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.19-1mdv2009.0
- first mdv release
