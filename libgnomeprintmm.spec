Summary:	C++ wrappers for libgnomeprint
Summary(pl):	Interfejsy C++ dla libgnomeprint
Name:		libgnomeprintmm
Version:	2.5.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	61db9f654329c01a0d1f7454eaab7864
URL:		http://www.gnome.org/
BuildRequires:	gtkmm-pango-devel >= 2.3.1
BuildRequires:	libgnomeprint-devel >= 2.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeprint.

%description -l pl
Interfejsy C++ dla libgnomeprint.

%package devel
Summary:	Devel files for libgnomeprintmm
Summary(pl):	Pliki nagłówkowe dla libgnomeprintmm
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	gtkmm-pango-devel >= 2.3.1

%description devel
Devel files for libgnomeprintmm.

%description devel -l pl
Pliki nagłówkowe dla libgnomeprintmm.

%package static
Summary:	libgnomeprintmm static library
Summary(pl):	Biblioteka statyczna libgnomeprintmm
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomeprintmm static library.

%description static -l pl
Biblioteka statyczna libgnomeprintmm.

%prep
%setup -q

%build
%configure \
	--enable-static=yes

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomeprintmm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeprintmm*.so
%{_libdir}/libgnomeprintmm*.la
%{_includedir}/%{name}-2.6
%{_libdir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeprintmm*.a
