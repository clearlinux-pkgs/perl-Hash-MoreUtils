#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Hash-MoreUtils
Version  : 0.06
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-0.06.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Hash-MoreUtils-0.06.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhash-moreutils-perl/libhash-moreutils-perl_0.05-2.debian.tar.xz
Summary  : 'Provide the stuff missing in Hash::Util'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Hash-MoreUtils-license = %{version}-%{release}
Requires: perl-Hash-MoreUtils-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
Hash::MoreUtils - Provide the stuff missing in Hash::Util
# SYNOPSIS
use Hash::MoreUtils qw(:all);

my %h = (foo => "bar", FOO => "BAR", true => 1, false => 0);
my %s = slice \%h, qw(true false); # (true => 1, false => 0)
my %f = slice_false \%h; # (false => 0)
my %u = slice_grep { $_ =~ m/^[A-Z]/ }, \%h; # (FOO => "BAR")

my %r = safe_reverse \%h; # (bar => "foo", BAR => "FOO", 0 => "false", 1 => "true")

%package dev
Summary: dev components for the perl-Hash-MoreUtils package.
Group: Development
Provides: perl-Hash-MoreUtils-devel = %{version}-%{release}
Requires: perl-Hash-MoreUtils = %{version}-%{release}

%description dev
dev components for the perl-Hash-MoreUtils package.


%package license
Summary: license components for the perl-Hash-MoreUtils package.
Group: Default

%description license
license components for the perl-Hash-MoreUtils package.


%package perl
Summary: perl components for the perl-Hash-MoreUtils package.
Group: Default
Requires: perl-Hash-MoreUtils = %{version}-%{release}

%description perl
perl components for the perl-Hash-MoreUtils package.


%prep
%setup -q -n Hash-MoreUtils-0.06
cd %{_builddir}
tar xf %{_sourcedir}/libhash-moreutils-perl_0.05-2.debian.tar.xz
cd %{_builddir}/Hash-MoreUtils-0.06
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Hash-MoreUtils-0.06/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Hash-MoreUtils
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Hash-MoreUtils/d175a490185516da33d4fd6260ec32d33c6a5487
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Hash::MoreUtils.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Hash-MoreUtils/d175a490185516da33d4fd6260ec32d33c6a5487

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
