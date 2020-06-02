# Global variables for github repository
%global commit0 150106e0e0d169d00173e6db8287db3d7a44f63e
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    yabridge
Version: 1.2.0
Release: 1%{?dist}
Summary: Yet another VST bridge
URL:     https://github.com/robbert-vdh/yabridge
Source0: https://github.com/robbert-vdh/yabridge/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:   Applications/Multimedia
License: GPLv2+

BuildRequires: gcc gcc-c++
BuildRequires: wine-devel
BuildRequires: meson
BuildRequires: boost-static
BuildRequires: libxcb-devel

%description
Yet another VST bridge

%prep
%setup -qn %{name}-%{commit0}

%build
mkdir build
meson setup --buildtype=release --cross-file cross-wine.conf build
VERBOSE=1 ninja -C build

%install

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_datadir}/*

%changelog