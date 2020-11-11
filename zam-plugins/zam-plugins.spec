# Global variables for github repository
%global commit0 8cd23d781018e3ec84159958d3d2dc7038a82736
%global gittag0 3.13
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commit1 08669d1bc30c6e971fde800eade4ca40104ba8b2
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:           zam-plugins
Version:        3.13
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
* Tue Nov 10 2020 Drew DeVore <drew@devorcula.com> - 3.13
- update to 3.13

* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 3.12
- update to 3.12

* Thu Jul 05 2018 Drew DeVore <drew@devorcula.com> - 3.10
- renamed to match Fedora conventions

* Sun May 06 2018 Drew DeVore <drew@devorcula.com> - 3.10
- update version to 3.10
- update for Fedora 28

* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 3.9
- update version to 3.9

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 3.5
- Initial build