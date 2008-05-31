%define module   Petal
%define version    2.19
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Perl Template Attribute Language
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(MKDoc::XML)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(CGI)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
examples deal with using Petal to generate HTML files from HTML templates.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Petal.pm
%perl_vendorlib/Petal

