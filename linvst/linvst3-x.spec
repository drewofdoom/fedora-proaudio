%global debug_package %{nil}

Name:           linvst3-x
Version:        2.15
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        Adds support for Windows VST3's to be used in Linux VST3 capable DAW's.

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/osxmidi/LinVst3-X
Source0:        https://github.com/osxmidi/LinVst3-X/releases/download/%{version}/LinVst3-X-%{version}-Debian-rz.zip
Requires:       /usr/bin/wine

%description
Adds support for Windows VST3's to be used in Linux VST3 capable DAW's.

%prep
%autosetup -n LinVst3-X-%{version}-Debian-rz

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/linvst3-x
mkdir -p %{buildroot}%{_datadir}/doc/linvst3-x
install -p -m 744 embedded/linvst3x.so %{buildroot}/%{_libdir}/linvst3-x/
install -p -m 755 embedded/lin-vst3-server* %{buildroot}/%{_bindir}
install -p -m 755 convert/linvst3xconvert* %{buildroot}/%{_bindir}
install -p -m 744 ReadMe %{buildroot}%{_datadir}/doc/linvst3-x/

%build

%clean

%files 
%doc ReadMe
%{_datadir}/doc/%{name}/
%{_libdir}/%{name}/linvst3x.so
%{_bindir}/lin-vst3-server*
%{_bindir}/linvst3xconvert*

%changelog
* Tue Nov 10 2020 Drew DeVore <drew@devorcula.com> - 2.15
- Update to 2.15

* Thu Sep 3 2020 Drew DeVore <drew@devorcula.com> - 2.0
- update to 2.0

* Tue Jun 2 2020 Drew DeVore <drew@devorcula.com> - 1.7.1
- update to 1.7.1

* Fri Mar 6 2020 Drew DeVore <drew@devorcula.com> - 1.7
- initial build
