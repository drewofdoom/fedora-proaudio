%global debug_package %{nil}

Name:           linvst
Version:        3.0
Release:        2%{?dist}
ExclusiveArch:  x86_64
Summary:        Adds support for Windows vst's to be used in Linux vst capable DAW's.

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/osxmidi/LinVst
Source0:        https://github.com/osxmidi/LinVst/releases/download/3.0/LinVst-%{version}-Debian-Stretch.zip
Requires:       /usr/bin/wine

%description
Adds support for Windows vst's to be used in Linux vst capable DAW's.

%prep
%autosetup -n LinVst-%{version}-Debian-Stretch

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/linvst
mkdir -p %{buildroot}%{_datadir}/doc/linvst
install -p -m 744 embedded/linvst.so %{buildroot}/%{_libdir}/linvst/
install -p -m 755 embedded/lin-vst-server* %{buildroot}/%{_bindir}
install -p -m 755 convert/linvstconvert* %{buildroot}/%{_bindir}
install -p -m 744 ReadMe %{buildroot}%{_datadir}/doc/linvst/

%clean

%files 
%doc ReadMe
%{_datadir}/doc/%{name}/
%{_libdir}/%{name}/linvst.so
%{_bindir}/lin-vst-server*
%{_bindir}/linvstconvert*

%changelog
* Thu Sep 3 2020 Drew DeVore <drew@devorcula.com> - 3.0
- Update to 3.0

* Fri Mar 6 2020 Drew DeVore <drew@devorcula.com> - 2.8
- Bumped release as package is not updating in COPR

* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 2.8
- Bump to 2.8

* Sun Sep 22 2019 Drew DeVore <drew@devorcula.com> - 2.7
- Bump to 2.7 and send linvst.so to /usr/share

* Thu Aug 29 2019 Drew DeVore <drew@devorcula.com> - 2.65
- Bump to 2.65

* Thu Aug 1 2019 Drew DeVore <drew@devorcula.com> - 2.6
- First package build
