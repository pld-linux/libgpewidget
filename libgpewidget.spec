Summary:	GPE widget library
Summary(pl.UTF-8):	Biblioteka widgetów GPE
Name:		libgpewidget
Version:	0.118
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	71d453d00aac718f32d0501372365794
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cairo-devel >= 0.4.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk-doc >= 1.2
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.23
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	cairo >= 0.4.0
Requires:	glib2 >= 1:2.6
Requires:	gtk+2 >= 2:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE widget library.

%description -l pl.UTF-8
Biblioteka widgetów GPE.

%package devel
Summary:	Header files for libgpewidget
Summary(pl.UTF-8):	Pliki nagłówkowe libgpewidget
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo-devel >= 0.4.0
Requires:	glib2-devel >= 1:2.6
Requires:	gtk+2-devel >= 2:2.4

%description devel
Header files for libgpewidget.

%description devel -l pl.UTF-8
Pliki nagłówkowe libgpewidget.

%package static
Summary:	Static libgpewidget library
Summary(pl.UTF-8):	Statyczna biblioteka libgpewidget
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpewidget library.

%description static -l pl.UTF-8
Statyczna biblioteka libgpewidget.

%package apidocs
Summary:	libgpewidget API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgpewidget
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgpewidget API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgpewidget.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/infoprint
%attr(755,root,root) %{_libdir}/libgpewidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpewidget.so.1
%dir %{_datadir}/libgpewidget
%{_datadir}/libgpewidget/clock.png
%{_datadir}/libgpewidget/clock24.png
%{_datadir}/libgpewidget/day-night-wheel.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpewidget.so
%{_libdir}/libgpewidget.la
%dir %{_includedir}/gpe
%{_includedir}/gpe/*.h
%{_pkgconfigdir}/libgpewidget.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpewidget.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgpewidget
