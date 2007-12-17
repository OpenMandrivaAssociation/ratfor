%define name ratfor
%define version 1.0.8
%define release %mkrel 3

Summary:		Ratfor fortran preprocessor
Name:			%name
Version:		%version
Release:		%release
License:		GPL
Group:			Development/Other

Requires(pre):		gcc-gfortran rpm-helper

Source0:		%{name}_1.0.orig.tar.bz2
# Short documentation from MIT
Source1:		ratfor.ps.bz2
# Patch from Debian
Patch0:			ratfor_1.0-8.diff

URL:			http://sepwww.stanford.edu/software/%{name}.html

ExclusiveArch:		%{ix86} ia64 x86_64 amd64

%description
Ratfor is preprocessor for FORTRAN code that allows us to use C-like 
flow expressions. From the Stanford Exploration Project.

%prep 
%setup -c 
bzcat %{SOURCE1} >%{name}.ps
ls -l
%patch -p0
mv ratfor-1.0.orig/* .
rmdir ratfor-1.0.orig

%build
%make -f Makefile

%install
mkdir -p $RPM_BUILD_ROOT/%_bindir
install -m755 ratfor $RPM_BUILD_ROOT/%_bindir
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
install -m644 ratfor.man $RPM_BUILD_ROOT/%_mandir/man1/ratfor.1

# (sb) installed but unpackaged
rm -f $RPM_BUILD_ROOT/ratfor.ps


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README %{name}.ps
%{_bindir}/*
%{_mandir}/man1/*


