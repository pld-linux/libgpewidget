#
Summary:	GPE widget library
Name:		libgpewidget
Version:	0.115
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://gpe.linuxtogo.org/download/source/%{name}-%{version}.tar.bz2
# Source0-md5:	88d53855c41fa7713263e913871a5fcc
URL:		http://gpe.linuxtogo.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libtool
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPE widget library.

%package devel
Summary:	Header files for libgpewidget
Group:		Development/Libraries

%description devel
Header files for libgpewidget.

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
%attr(755,root,root) %{_libdir}/libgpewidget.so.1.0.0
%dir %{_datadir}/libgpewidget
%{_datadir}/libgpewidget/clock.png
%{_datadir}/libgpewidget/clock24.png
%{_datadir}/libgpewidget/day-night-wheel.png

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gpe
%{_includedir}/gpe/*.h
%{_libdir}/libgpewidget.la
%{_libdir}/libgpewidget.so
%{_pkgconfigdir}/libgpewidget.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpewidget.a
