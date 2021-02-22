# Global variables for github repository
%global commit0 78b0307afeded440c80a2b1d732dd15382f7b335
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


%global debug_package %{nil}

Name:           Catia
Version:        git78b0307
Release:        2%{?dist}
Summary:        A JACK patchbay
URL:            https://github.com/falkTX/Catia
Source0:        https://github.com/falkTX/Catia/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Group:          Applications/Multimedia
License:        GPLv2+
BuildRequires:  python3-qt5-base
Requires:       python3-qt5
Requires:       (jack-audio-connection-kit or pipewire-jack-audio-connection-kit)

%description
A JACK patchbay

%prep
%autosetup -n %{name}-%{commit0}

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
mkdir -p %{buildroot}/%{_datadir}/catia/jacklib
mkdir -p %{buildroot}/%{_datadir}/catia/patchcanvas
install -m 644 data/*.desktop               %{buildroot}/%{_datadir}/applications/
install -m 644 resources/16x16/catia.png    %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/
install -m 644 resources/48x48/catia.png    %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/
install -m 644 resources/128x128/catia.png  %{buildroot}/%{_datadir}/icons/hicolor/128x128/apps/
install -m 644 resources/256x256/catia.png  %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
install -m 644 resources/scalable/catia.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/
install -m 755 src/*.py                     %{buildroot}/%{_datadir}/catia/
install -m 755 src/jacklib/*.py             %{buildroot}/%{_datadir}/catia/jacklib/
install -m 755 src/patchcanvas/*.py         %{buildroot}/%{_datadir}/catia/patchcanvas/
sed -i "s?X-PREFIX-X?%{_datadir}?" data/catia
install -m 755 data/catia                   %{buildroot}/%{_bindir}/catia

%files
%{_datadir}/applications/
%{_datadir}/icons/hicolor/16x16/apps/
%{_datadir}/icons/hicolor/48x48/apps/
%{_datadir}/icons/hicolor/128x128/apps/
%{_datadir}/icons/hicolor/256x256/apps/
%{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/catia/
%{_datadir}/catia/jacklib/
%{_datadir}/catia/patchcanvas/
%{_bindir}/catia

%changelog
* Mon Feb 22 2021 Drew DeVore <drew@devorcula.com> - 78b0307afeded440c80a2b1d732dd15382f7b335
- fix launch script before installing

* Mon Feb 22 2021 Drew DeVore <drew@devorcula.com> - 78b0307afeded440c80a2b1d732dd15382f7b335
- initial build