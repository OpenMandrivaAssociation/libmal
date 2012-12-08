%define major   	1
%define libname 	%mklibname mal %{major}
%define develname	%mklibname mal -d

Name: 			libmal
Version: 		0.44.1
Release: 		%mkrel 6
Group: 			System/Libraries
License: 		MPL
URL: 			http://www.jlogday.com/code/libmal/
Source: 		http://www.jlogday.com/code/libmal/%{name}-%{version}.tar.gz
Patch1:			libmal-0.44-lib64.patch
Patch2:			libmal-0.44-libtool.patch
Patch3:			libmal-0.44-64bit-fixes.patch
Summary: 		MAL library for AvantGo
BuildRoot: 		%{_tmppath}/%{name}-buildroot
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
The %{name}-devel package includes the header files and libraries
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

%build
autoreconf -fi
%configure2_5x --disable-static
%make

%install
%make DESTDIR=%{buildroot} install
# Remove unpackaged copy of README
rm -f %{buildroot}%{_docdir}/libmal1/README

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%clean
rm -rf %{buildroot}

%files malsync
%defattr(-,root,root,-)
%_bindir/malsync

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%_includedir/libmal
%{_libdir}/*.so


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.44.1-3mdv2011.0
+ Revision: 661496
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.44.1-2mdv2011.0
+ Revision: 602574
- rebuild

* Thu Apr 22 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.44.1-1mdv2010.1
+ Revision: 538000
- new version 0.44.1
  disabled static build
  updated Url and Source

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.44-7mdv2010.1
+ Revision: 520883
- rebuilt for 2010.1

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 0.44-6mdv2010.0
+ Revision: 453768
- rebuild for new location of libusb

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.44-5mdv2010.0
+ Revision: 425596
- rebuild

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.44-4mdv2009.1
+ Revision: 365614
- rediff 64bit fixes patch
- reidff libtool patch

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.44-4mdv2009.0
+ Revision: 222926
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 0.44-3mdv2008.1
+ Revision: 189656
- Fix group
- protect major

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.44-2mdv2008.1
+ Revision: 150706
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 0.44-1mdv2008.0
+ Revision: 55239
- rebuild for 2008
- new devel policy
- spec clean
- now includes a malsync binary, so use this one and obsolete malsync package
- rediff patches
- new release 0.44
- Import libmal




* Tue Sep 05 2006 Frederic Crozat <fcrozat@mandriva.com> 0.31-9mdv2007.0
- Patch4: use pilot-link 0.12 API

* Sun Jan 01 2006 Mandrake Linux KDE Team <kde@mandrakesoft.com> 0.31-8mdk
- Rebuild

* Fri Nov 05 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-7mdk
- Rebuild

* Thu Oct 23 2003 Stefan van der Eijk <stefan@eijk.nu> 0.31-6mdk
- BuildRequires

* Fri Sep  5 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.31-5mdk
- lib64 & libtool fixes

* Thu Jul 10 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-4mdk
- Rebuild

* Wed Jul 09 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-3mdk
- Fix requires

* Wed Jul 09 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-2mdk
- Rebuild

* Mon Jul 07 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.31-1mdk
- Update 0.31 (thanks Texstar to point me it)

* Mon Apr 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-3mdk
- Fix spec file

* Fri Dec 20 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-2mdk
- Fix compile

* Tue Dec 17 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.20-1mdk
- Initial package, initial spec file by ShavenYak <shavenyak@smith.dyndns.org>
