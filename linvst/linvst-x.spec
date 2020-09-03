%global debug_package %{nil}

Name:           linvst-x
Version:        3.0.0
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        Adds support for Windows vst's to be used in Linux vst capable DAW's.

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/osxmidi/LinVst
Source0:        https://github.com/osxmidi/LinVst-X/releases/download/3.0/LinVst-X-%{version}-Debian-Buster.zip
Requires:       /usr/bin/wine

%description
Adds support for Windows vst's to be used in Linux vst capable DAW's.

%prep
%autosetup -n LinVst-X-%{version}-Debian-Buster

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/linvst-x
mkdir -p %{buildroot}%{_datadir}/doc/linvst-x
install -p -m 744 embedded/linvstx.so %{buildroot}/%{_libdir}/linvst-x/
install -p -m 755 embedded/lin-vst-server* %{buildroot}/%{_bindir}
install -p -m 755 convert/linvstxconvert* %{buildroot}/%{_bindir}
install -p -m 744 ReadMe %{buildroot}%{_datadir}/doc/linvst-x/

%clean

%files 
%doc ReadMe
%{_datadir}/doc/%{name}/
%{_libdir}/%{name}/linvstx.so
%{_bindir}/lin-vst-server*
%{_bindir}/linvstxconvert*

%changelog
* Thu Sep 3 2020 Drew DeVore <drew@devorcula.com> - 3.0
- Update to 3.0
* Tue Jun 2 2020 Drew DeVore <drew@devorcula.com> - 2.7.1
- Update to 2.7.1
* Fri Mar 6 2020 Drew DeVore <drew@devorcula.com> - 2.7
- Initial version
