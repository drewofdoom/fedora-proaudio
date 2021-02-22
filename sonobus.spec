%global debug_package %{nil}

Name:           sonobus
Version:        1.3.2
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        SonoBus is an easy to use application for streaming high-quality, low-latency peer-to-peer audio between devices over the internet or a local network.

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/essej/sonobus
Source0:        https://github.com/essej/sonobus/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:       libopusenc
Requires:       jack-audio-connection-kit
BuildRequires:  libopusenc-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  freetype-devel
BuildRequires:  libcurl-devel

%description
SonoBus is an easy to use application for streaming high-quality, low-latency peer-to-peer audio between devices over the internet or a local network.

%prep
%autosetup

%build
cd Builds/LinuxMakefile
CONFIG=Release make -j$(nproc) Standalone VST3

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/vst3/SonoBus.vst3/Contents/x86_64-linux
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p -m 744 Builds/LinuxMakefile/build/SonoBus %{buildroot}/%{_bindir}/SonoBus
install -p -m 744 Builds/LinuxMakefile/build/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so %{buildroot}/%{_libdir}/vst3/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so
install -p -m 644 images/sonobus_logo@2x.png %{buildroot}/%{_datadir}/pixmaps/sonobus.png
install -p -m 644 Builds/LinuxMakefile/sonobus.desktop %{buildroot}/%{_datadir}/applications/sonobus.desktop

%clean

%files
%{_bindir}/SonoBus
%{_libdir}/vst3/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so
%{_datadir}/pixmaps/sonobus.png
%{_datadir}/applications/sonobus.desktop

%changelog
* Sun Feb 21 2021 Drew DeVore <drew@devorcula.com> - 1.3.2
- Initial build