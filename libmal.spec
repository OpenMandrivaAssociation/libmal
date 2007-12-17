%define name    	libmal
%define version 	0.44
%define release 	%mkrel 1
%define major   	1
%define libname 	%mklibname mal %{major}
%define develname	%mklibname mal -d

Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Group: 			Communications
License: 		MPL
URL: 			http://jasonday.home.att.net/code/libmal/libmal.html
Source: 		http://jasonday.home.att.net/code/libmal/%{name}-%{version}.tar.gz
Patch1:			libmal-0.44-lib64.patch
Patch2:			libmal-0.44-libtool.patch
Patch3:			libmal-0.31-64bit-fixes.patch
Summary: 		MAL library for AvantGo
Requires: 		pilot-link
BuildRequires:		autoconf
BuildRequires: 		pilot-link-devel >= 0.12.0

%package -n 	%{libname}
Summary:        MAL library for AvantGo
Group:          System/Libraries

%description 
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.


%description -n %{libname}
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions. 


%package -n 	%{develname}
Summary:        Development tools for programs which will use the %{name} library
Group:          Development/C
Requires:   	%{libname} = %{version}-%release
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname mal 0 -d}

%description -n %{develname}
The %{name}-devel package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install %{name}-devel.  You'll also need to have the %name
package installed.

%package	malsync
Summary:	Utility to update Palms from Avantgo and MobileLink web site
Group:		Communications
Obsoletes:	malsync
Provides:	malsync

%description malsync
Malsync is a tool for updating Palm devices from the AvantGo and
MobileLink web sites.

%prep
%setup -q
%patch1 -p1 -b .lib64
%patch2 -p1 -b .libtool
%patch3 -p1 -b .64bit-fixes
autoconf

%build
%configure2_5x
%make

%install
%make DESTDIR=$RPM_BUILD_ROOT install
# Remove unpackaged copy of README
rm -f %{buildroot}%{_docdir}/libmal1/README

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT

%files malsync
%defattr(-,root,root,-)
%_bindir/malsync

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%_includedir/libmal
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
