%global debug_package %{nil}

Name:           linvst3
Version:        1.8
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
mkdir -p %{buildroot}/%{_libdir}/linvst
mkdir -p %{buildroot}%{_datadir}/doc/linvst
mkdir -p %{buildroot}%{_datadir}/linvst
install -p -m 744 embedded/linvst.so %{buildroot}/%{_datadir}/linvst/
install -p -m 755 embedded/lin-vst-server* %{buildroot}/%{_bindir}
install -p -m 755 convert/linvstconvert* %{buildroot}/%{_bindir}
install -p -m 744 ReadMe %{buildroot}%{_datadir}/doc/linvst/

%clean

%files 
%doc ReadMe
%{_datadir}/doc/%{name}/
%{_datadir}/%{name}/linvst3.so
%{_bindir}/lin-vst3-server*
%{_bindir}/linvst3convert*

%changelog
* Mon Mar 2 2020 Drew DeVore <drew@devorcula.com> - 1.8
- initial build
