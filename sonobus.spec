%global forgeurl    https://github.com/essej/sonobus
%global tag         %{version}
%forgemeta

Name:           sonobus
Version:        1.3.2
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        Application for streaming audio between devices
License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(opus)

Requires:       libopusenc
Requires:       (jack-audio-connection-kit or pipewire-jack-audio-connection-kit)
BuildRequires:  libopusenc-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  mesa-libGL-devel

%description
SonoBus is an easy to use application for streaming high-quality, low-latency
peer-to-peer audio between devices over the internet or a local network.

%prep
%forgeautosetup

%build
%set_build_flags
cd Builds/LinuxMakefile
%make_build Standalone VST3 CONFIG=Release

%install
install -D -p -m 755 Builds/LinuxMakefile/build/SonoBus %{buildroot}%{_bindir}/SonoBus
install -D -p -m 744 Builds/LinuxMakefile/build/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so %{buildroot}%{_libdir}/vst3/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so
install -D -p -m 644 images/sonobus_logo@2x.png %{buildroot}%{_datadir}/pixmaps/sonobus.png
install -D -p -m 644 Builds/LinuxMakefile/sonobus.desktop %{buildroot}%{_datadir}/applications/sonobus.desktop

%files
%{_bindir}/SonoBus
%{_libdir}/vst3/SonoBus.vst3/Contents/x86_64-linux/SonoBus.so
%{_datadir}/pixmaps/sonobus.png
%{_datadir}/applications/sonobus.desktop

%changelog
* Sun Feb 21 2021 Drew DeVore <drew@devorcula.com> - 1.3.2
- Initial build