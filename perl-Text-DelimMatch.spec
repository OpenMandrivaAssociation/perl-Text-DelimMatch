%define realname  Text-DelimMatch
%define preversion a

Name:		perl-%{realname}
Version:    1.06
Release:    %mkrel 4
License:	GPL
Group:		Development/Perl
Summary:    Perl extension to find regexp delimited strings with proper nesting
Source0:    http://search.cpan.org/CPAN/authors/id/N/NW/NWALSH/DelimMatch-%{version}%{preversion}.tar.bz2
Url:		http://search.cpan.org/dis/DelimMatch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildArch: noarch

%description
These routines allow you to match delimited substrings in a buffer.
The delimiters can be specified with any regular expression and the
start and end delimiters need not be the same. If the delimited text
is properly nested, entire nested groups are returned.

In addition, you may specify quoting and escaping characters that 
contribute to the recognition of start and end delimiters.

%prep
%setup -q -n DelimMatch-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*

