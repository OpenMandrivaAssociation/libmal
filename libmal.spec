%define	major	1
%define	libname	%mklibname mal %{major}
%define	devname	%mklibname mal -d

Summary: 		MAL library for AvantGo
Name:			libmal
Version:		0.44.1
Release:		17
Group:			System/Libraries
License:		MPL
Url:			https://www.jlogday.com/code/libmal/
Source0:		http://www.jlogday.com/code/libmal/%{name}-%{version}.tar.gz
Patch1:			libmal-0.44-lib64.patch
Patch2:			libmal-0.44-libtool.patch
Patch3:			libmal-0.44-64bit-fixes.patch
Patch4:			libmal-0.44.1-automake-1.13-fix.patch
BuildRequires: 		pkgconfig(pilot-link)
Requires: 		pilot-link

%description 
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions.

%package -n		%{libname}
Summary:		MAL library for AvantGo
Group:			System/Libraries

%description -n	%{libname}
libmal is really just a convenience library of the functions in Tom
Whittaker's malsync distribution, along with a few wrapper functions. 

%package -n	%{devname}
Summary:	Development tools for programs which will use the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}-%release
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package includes the header files and libraries
necessary for developing programs using the %{name} library.

%package	malsync
Summary:	Utility to update Palms from Avantgo and MobileLink web site
Group:		Communications

%description	malsync
Malsync is a tool for updating Palm devices from the AvantGo and
MobileLink web sites.

%prep
%setup -q
%autopatch -p1
autoreconf -fi

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files malsync
%{_bindir}/malsync

%files -n %{libname}
%{_libdir}/libmal.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/libmal
%{_libdir}/libmal.so

