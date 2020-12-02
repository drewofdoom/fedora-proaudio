%global debug_package %{nil}

Name:    yabridge
Version: 2.1.0
Release: 1%{?dist}
Summary: Yet another VST bridge
URL:     https://github.com/robbert-vdh/yabridge
Source0: https://github.com/robbert-vdh/yabridge/releases/download/%{version}/%{name}-%{version}.tar.gz
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
%autosetup

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
* Wed Dec 02 2020 drew DeVore <drew@devorcula.com> - 2.1.0
- Update to 2.0.1

* Tue Nov 10 2020 drew DeVore <drew@devorcula.com> - 2.0.1
- Update to 2.0.1

* Thu Oct 1 2020 drew DeVore <drew@devorcula.com> - 1.6.1
- Update to 1.6.1