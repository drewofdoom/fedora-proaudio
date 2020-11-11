%global debug_package %{nil}

Name:           linvst3
Version:        2.15
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        Adds support for Windows VST3's to be used in Linux VST3 capable DAW's.

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/osxmidi/LinVst3
Source0:        https://github.com/osxmidi/LinVst3/releases/download/%{version}/LinVst3-%{version}-Debian-Stretch.zip
Requires:       /usr/bin/wine

%description
Adds support for Windows VST3's to be used in Linux VST3 capable DAW's.

%prep
%autosetup -n LinVst3-%{version}-Debian-Stretch

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/linvst3
mkdir -p %{buildroot}%{_datadir}/doc/linvst3
install -p -m 744 embedded/linvst3.so %{buildroot}/%{_libdir}/linvst3/
install -p -m 755 embedded/lin-vst3-server* %{buildroot}/%{_bindir}
install -p -m 755 convert/linvst3convert* %{buildroot}/%{_bindir}
install -p -m 744 ReadMe %{buildroot}%{_datadir}/doc/linvst3/

%build

%clean

%files 
%doc ReadMe
%{_datadir}/doc/%{name}/
%{_libdir}/%{name}/linvst3.so
%{_bindir}/lin-vst3-server*
%{_bindir}/linvst3convert*

%changelog
* Tue Nov 10 2020 Drew DeVore <drew@devorcula.com> - 2.15
- Update to 2.15

* Thu Oct 1 2020 Drew DeVore <drew@devorcula.com> - 2.1
- Update to 2.1

* Thu Sep 3 2020 Drew DeVore <drew@devorcula.com> - 2.0
- Update to 2.0

* Fri Mar 6 2020 Drew DeVore <drew@devorcula.com> - 1.8
- Bumped release to fix libdir

* Mon Mar 2 2020 Drew DeVore <drew@devorcula.com> - 1.8
- initial build
