Summary:	C++ wrappers for libgnomeprint
Summary(pl.UTF-8):	Interfejsy C++ dla libgnomeprint
Name:		libgnomeprintmm
Version:	2.5.1
Release:	5
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomeprintmm/2.5/%{name}-%{version}.tar.bz2
# Source0-md5:	cac1729ff8708bec30be4291b73530bc
URL:		http://www.gnome.org/
BuildRequires:	libgnomeprint-devel >= 2.6.1
BuildRequires:	pangomm-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for libgnomeprint.

%description -l pl.UTF-8
Interfejsy C++ dla libgnomeprint.

%package devel
Summary:	Devel files for libgnomeprintmm
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgnomeprintmm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgnomeprint-devel >= 2.6.1
Requires:	pangomm-devel

%description devel
Devel files for libgnomeprintmm.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libgnomeprintmm.

%package static
Summary:	libgnomeprintmm static library
Summary(pl.UTF-8):	Biblioteka statyczna libgnomeprintmm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomeprintmm static library.

%description static -l pl.UTF-8
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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libgnomeprintmm-2.5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomeprintmm-2.5.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomeprintmm-2.5.so
%{_includedir}/%{name}-2.6
%{_libdir}/%{name}-2.6
%{_pkgconfigdir}/%{name}-2.6.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomeprintmm-2.5.a
