%global vst3_plugin SonoBus.vst3/Contents/%(uname -m)-linux/SonoBus.so
%global forgeurl    https://github.com/essej/sonobus
%global tag         %{version}
%forgemeta
Name:           sonobus
Version:        1.4.3
Release:        2%{?dist}
Summary:        Application for streaming audio between devices
# main source code is GPLv3
# deps/aoo is BSD
# deps/ff_meters is BSD
# deps/juce is ISC and GPLv3
License:        GPLv3 and BSD and ISC
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib alsa-lib-devel
BuildRequires:  freetype-devel
BuildRequires:  curl-devel
BuildRequires:  opus-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  mesa-libGL-devel
Provides:       bundled(aoo) = 2.0.0
Provides:       bundled(ff_meters) = 0.9.1
Provides:       bundled(juce) = 6.0.4

%description
SonoBus is an easy to use application for streaming high-quality, low-latency
peer-to-peer audio between devices over the internet or a local network.

%package vst3
Summary:        %{name} VST3 plugin

%description vst3
%{name} VST3 plugin.
%prep

%forgeautosetup
cp deps/aoo/LICENSE LICENSE-aoo
cp deps/ff_meters/LICENSE.md LICENSE-ff_meters.md
cp deps/juce/LICENSE.md LICENSE-juce.md

%build
%set_build_flags
cd Builds/LinuxMakefile
%make_build Standalone VST3 CONFIG=Release

%install
install -D -p -m 755 Builds/LinuxMakefile/build/SonoBus %{buildroot}%{_bindir}/SonoBus
install -D -p -m 644 images/sonobus_logo@2x.png %{buildroot}%{_datadir}/pixmaps/sonobus.png
install -D -p -m 644 Builds/LinuxMakefile/sonobus.desktop %{buildroot}%{_datadir}/applications/sonobus.desktop
# https://steinbergmedia.github.io/vst3_doc/vstinterfaces/vst3loc.html#linuxformat
# https://steinbergmedia.github.io/vst3_doc/vstinterfaces/vst3loc.html#linuxlocation
install -D -p -m 755 Builds/LinuxMakefile/build/%{vst3_plugin} %{buildroot}%{_libdir}/vst3/%{vst3_plugin}

%files
%license LICENSE LICENSE-aoo LICENSE-ff_meters.md LICENSE-juce.md
%{_bindir}/SonoBus
%{_datadir}/pixmaps/sonobus.png
%{_datadir}/applications/sonobus.desktop
%files vst3
%license LICENSE LICENSE-aoo LICENSE-ff_meters.md LICENSE-juce.md
%dir %{_libdir}/vst3
%{_libdir}/vst3/%{vst3_plugin}

%changelog
* Sat Apr 10 2021 Drew DeVore <drew@devorcula.com> - 1.4.3
- bump version to 1.4.3

* Wed Feb 24 2021 Drew DeVore <drew@devorcula.com> - 1.3.2
- Merged changes from Carl and Sally
- Reconfigured

* Wed Feb 24 2021 Sally Haj <sallyahaj@autistici.org> - 1.3.2
- Applied fixes and emailed to Drew DeVore

* Wed Feb 24 2021 Carl George <carl@george.computer> - 1.3.2
- Applied fixes and submitted PR

* Sun Feb 21 2021 Drew DeVore <drew@devorcula.com> - 1.3.2
- Initial build