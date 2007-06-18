Summary:	GPE widget library
Summary(pl.UTF-8):	Biblioteka widgetów GPE
Name:		libgpewidget
Version:	0.115
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	88d53855c41fa7713263e913871a5fcc
Source1:	%{name}.pl.po
URL:		http://gpe.linuxtogo.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.4
BuildRequires:	intltool >= 0.23
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
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

%prep
%setup -q

cp %{SOURCE1} po/pl.po
sed -i -e 's/nl pt/nl pl pt/' configure.ac

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
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
