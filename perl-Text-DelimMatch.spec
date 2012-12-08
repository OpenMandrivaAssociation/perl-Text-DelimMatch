%define realname  Text-DelimMatch
%define preversion a

Name:		perl-%{realname}
Version:    1.06
Release:    %mkrel 10
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/*
%{_mandir}/man3/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.06-10mdv2012.0
+ Revision: 765756
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.06-9
+ Revision: 764261
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.06-8
+ Revision: 763285
- force it
- rebuild

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.06-7
+ Revision: 654323
- rebuild for updated spec-helper

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.06-6mdv2011.0
+ Revision: 426594
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.06-5mdv2009.1
+ Revision: 351714
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.06-4mdv2009.0
+ Revision: 224205
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.06-3mdv2008.1
+ Revision: 151360
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.06-2mdv2008.0
+ Revision: 23305
- rebuild


* Sat Nov 05 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.06-1mdk
- First Mandriva package

