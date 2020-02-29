# Global variables for github repository
%global commit0 87fdee6e87dbee75c1088e2327ea59c1ab1522e4
%global gittag0 3.12
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 68b3a57a78d814810972584ed571662fe5cfb8f0
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           zam-plugins
Version:        3.12
Release:        1%{?dist}
Summary:        Zam set of plugins

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/zamaudio/zam-plugins/
Source0:        https://github.com/zamaudio/zam-plugins/archive/%{version}.tar.gz#/zam-plugins-%{version}.tar.gz
Source1:        https://github.com/DISTRHO/DPF/archive/%{commit1}/DPF-%{commit1}.tar.gz

BuildRequires: lv2-devel
BuildRequires: mesa-libGL-devel
BuildRequires: fftw-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: liblo-devel
BuildRequires: mesa-libGL-devel
BuildRequires: gcc-c++
BuildRequires: libX11-devel
BuildRequires: libGL-devel
BuildRequires: ladspa-devel
BuildRequires: libsamplerate-devel

%description
Zam LV2 set of plugins

%package common
Summary:        Common files for the Zam plugins
Group:          Applications/Multimedia

%description common
Common files for the Zam plugins

%package -n lv2-zam-plugins
Summary:        Zam LV2 plugins
Group:          Applications/Multimedia
Requires:       zam-plugins-common

%description -n lv2-zam-plugins
Zam LV2 plugins

%package -n ladspa-zam-plugins
Summary:        Zam LADSPA plugins
Group:          Applications/Multimedia
Requires:       zam-plugins-common

%description -n ladspa-zam-plugins
Zam LADSPA plugins

%package -n vst-zam-plugins
Summary:        Zam VST plugins
Group:          Applications/Multimedia
Requires:       zam-plugins-common

%description -n vst-zam-plugins
Zam VST plugins

%prep
%autosetup -n zam-plugins-%{version}
%autosetup -n zam-plugins-%{version} -a 1
rmdir dpf
mv ./DPF-%{commit1} ./dpf 

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}
make DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} install

%files common
%{_bindir}/*

%files -n lv2-zam-plugins
%{_libdir}/lv2/*

%files -n ladspa-zam-plugins
%{_libdir}/ladspa/* 

%files -n vst-zam-plugins
%{_libdir}/vst/* 

%changelog
* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 3.12
- update to 3.12

* Sun Jul 05 2018 Drew DeVore <drew@devorcula.com> - 3.10
- renamed to match Fedora conventions

* Sun May 06 2018 Drew DeVore <drew@devorcula.com> - 3.10
- update version to 3.10
- update for Fedora 28

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build