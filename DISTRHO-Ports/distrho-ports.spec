%global debug_package %{nil}

Name:           distrho-ports
Version:        20200714git
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        A collection of audio plugins

Group:          Applications/Multimedia
License:        MIT
URL:            https://github.com/DISTRHO/DISTRHO-Ports
Source0:        https://github.com/DISTRHO/DISTRHO-Ports/archive/2020-07-14.tar.gz
BuildRequires:  meson
BuildRequires:  alsa-lib-devel
BuildRequires:  freetype-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxshmfence-devel

%description
A collection of audio plugins

%package -n lv2-distrho-ports
Summary:        A collection of LV2 plugins
Group:          Applications/Multimedia

%description -n lv2-distrho-ports
A collection of LV2 plugins

%package -n vst-distrho-ports
Summary:        A collection of VST plugins
Group:          Applications/Multimedia

%description -n vst-distrho-ports
A collection of VST plugins

%prep
rm -rf %{name}-%{version}
tar -xvf %{_sourcedir}/2020-07-14.tar.gz
if [ $? -ne 0 ]; then
  exit $?
fi
mv DISTRHO-Ports-2020-07-14 %{name}-%{version}
cd %{name}-%{version}

%build
cd %{name}-%{version}
meson build --buildtype release
ninja -C build

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_libdir}/lv2/
mkdir -p %{buildroot}%{_libdir}/vst/
mv %{_builddir}/%{name}-%{version}/build/ports-legacy/*.lv2 %{buildroot}%{_libdir}/lv2/
install -p -m 744 %{_builddir}/%{name}-%{version}/build/ports-legacy/*.so %{buildroot}%{_libdir}/vst/

%clean

%files -n lv2-distrho-ports
%{_libdir}/lv2/

%files -n vst-distrho-ports
%{_libdir}/vst/

%changelog
* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 20200223
- initial build