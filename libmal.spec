%define name    libmal
%define version 0.31
%define release %mkrel 9
%define major   0
%define lib_name %mklibname mal %{major}

Name: 			%name
Version: 		%version
Release: 		%release
Group: 			Communications
License: 		MPL
Packager: 		Mandriva Linux KDE Team <kde@mandriva.com>
URL: 			http://jasonday.home.att.net/code/libmal/libmal.html
Source: 		libmal-%{version}.tar.bz2
Patch: 			libmal-0.20-install.patch.bz2
Patch1:			libmal-0.31-lib64.patch.bz2
Patch2:			libmal-0.31-libtool.patch.bz2
Patch3:			libmal-0.31-64bit-fixes.patch.bz2
# (fc) 0.31-9mdv use pilot-link 0.12 API
Patch4:			libmal-0.31-pilotlink012.patch.bz2
Summary: 		MAL library for AvantGo
BuildRoot: 		%{_tmppath}/%{name}-buildroot
Requires: 		pilot-link
BuildRequires:	autoconf2.5
BuildRequires: 	pilot-link-devel >= 0.12.0

%package -n 	%{lib_name}
Summary:        MAL library for AvantGo
Group:          System/Libraries

%description 
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.


%description -n %{lib_name}
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions. 


%package -n 	%{lib_name}-devel
Summary:        Development tools for programs which will use the %{name} library.
Group:          Development/C
Requires:   	%{lib_name} = %{version}-%release
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
The %{name}-devel package includes the header files and static libraries
necessary for developing programs using the %{name} library.

If you are going to develop programs which will use the %{name} library
you should install %{name}-devel.  You'll also need to have the %name
package installed.


%prep
%setup -q
#%patch -p1
%patch1 -p1 -b .lib64
%patch2 -p1 -b .libtool
%patch3 -p1 -b .64bit-fixes
%patch4 -p1 -b .pilotlink012
autoconf

%build
%configure2_5x
%make

%install
%make DESTDIR=$RPM_BUILD_ROOT install


%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%dir %_includedir/libmal/
%_includedir/libmal/*.h
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.so
