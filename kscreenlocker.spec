Summary:	Library and components for secure lock screen architecture
Name:		kscreenlocker
Version:	5.5.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		http://kde.org/
Source0:	http://download.kde.org//%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	pam-devel
Conflicts:      plasma-workspace < 5.5.0

%description
Library and components for secure lock screen architecture. 

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files

