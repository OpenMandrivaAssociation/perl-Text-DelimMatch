%define modname  Text-DelimMatch
%define preversion a

Summary:	Perl extension to find regexp delimited strings with proper nesting
Name:		perl-%{modname}
Version:	1.06
Release:	20
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dis/DelimMatch
Source0:	http://search.cpan.org/CPAN/authors/id/N/NW/NWALSH/DelimMatch-%{version}%{preversion}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
These routines allow you to match delimited substrings in a buffer.
The delimiters can be specified with any regular expression and the
start and end delimiters need not be the same. If the delimited text
is properly nested, entire nested groups are returned.

In addition, you may specify quoting and escaping characters that 
contribute to the recognition of start and end delimiters.

%prep
%setup -qn DelimMatch-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

