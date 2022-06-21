%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Library and components for secure lock screen architecture
Name:		kscreenlocker
Version:	5.25.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://kde.org/
Source0:	http://download.kde.org//%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
Patch0:		kscreenlocker-5.5.3-use-fallback-wallpaper-from-omv.patch
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=1319
Patch1:		kscreenlocker-5.5.3-add-missing-library.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(libseccomp)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(LayerShellQt)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	wayland-tools
BuildRequires:	pam-devel
Conflicts:      plasma-workspace < 5.5.0

%description
Library and components for secure lock screen architecture.

%triggerin -- %{name} < %{EVRD}
%{_bindir}/killall kscreenlocker_greet > /dev/null 2>&1 ||:

%files -f kscreenlocker.lang -f kscreenlocker_greet.lang -f kcm_screenlocker.lang
%{_libdir}/libexec/kscreenlocker_greet
%{_datadir}/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
%{_datadir}/kconf_update/kscreenlocker.upd
%{_datadir}/kconf_update/ksreenlocker_5_3_separate_autologin.pl
%{_datadir}/knotifications5/ksmserver.notifyrc
%{_datadir}/ksmserver/screenlocker/org.kde.passworddialog
%{_datadir}/dbus-1/interfaces/org.kde.screensaver.xml
%{_datadir}/kpackage/kcms/kcm_screenlocker
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_datadir}/applications/kcm_screenlocker.desktop

#--------------------------------------------------------------------

%define kscreenlocker_major 5
%define libkscreenlocker %mklibname kscreenlocker %{kscreenlocker_major}

%package -n %{libkscreenlocker}
Summary:	Library and components for secure lock screen architecture 
Group:		System/Libraries

%description -n %{libkscreenlocker}
Library and components for secure lock screen architecture.

%files -n %{libkscreenlocker}
%{_libdir}/libKScreenLocker.so.%{kscreenlocker_major}*

#--------------------------------------------------------------------

%define kscreenlocker_devel %mklibname kscreenlocker -d

%package -n %{kscreenlocker_devel}
Summary:        Devel stuff for %{name}
Group:          Development/KDE and Qt
Requires:       %{name} = %{EVRD}
Requires:       %{libkscreenlocker} = %{EVRD}
Requires:       pkgconfig(Qt5DBus)
Provides:       %{name}-devel = %{EVRD}

%description -n %{kscreenlocker_devel}
This package contains header files needed if you wish to build applications
based on %{name}.

%files -n %{kscreenlocker_devel}
%{_libdir}/libKScreenLocker.so
%{_includedir}/KScreenLocker
%{_libdir}/cmake/KScreenLocker
%{_libdir}/cmake/ScreenSaverDBusInterface

#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kscreenlocker || touch kscreenlocker.lang
%find_lang kscreenlocker_greet || touch kscreenlocker_greet.lang
%find_lang kcm_screenlocker || touch kcm_screenlocker.lang
