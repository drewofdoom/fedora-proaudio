%global debug_package %{nil}

%global commit0 abdedd527e6e1cf86636f0f1e8a3e75b06ed166a
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           helm
Version:        20180608git
Release:        1%{?dist}
Summary:        A standalone synth

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/mtytel/helm
Source0:        https://github.com/mtytel/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Requires:      %{name}-common = %{version}-%{release}

BuildRequires: gcc gcc-c++
BuildRequires: liblo-devel
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: mesa-libGL-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: freetype-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libcurl-devel

%description
A standalone synth

%package common
Summary:        Common files for Helm synthesizers
Group:          Applications/Multimedia

%description common
Common files for Helm synthesizers

%package -n lv2-helm
Summary:        LV2 version of the Helm synth
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}
Requires:       lv2

%description -n lv2-helm
LV2 version of the Helm synth

%package -n vst-helm
Summary:        VST version of the Helm synth
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}

%description -n vst-helm
VST version of the Helm synth

%prep
%setup -qn %{name}-%{commit0}

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "114,125d" JUCE/modules/juce_graphics/colour/juce_PixelFormats.h
%endif

sed -i "s/\/lib\//\/lib64\//g" Makefile

%build
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags}

%install 
make DESTDIR=%{buildroot} standalone lv2 %{?_smp_mflags} install

%post 
update-desktop-database -q
touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :

%postun
update-desktop-database -q
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/hicolor >&/dev/null || :
  gtk-update-icon-cache %{_datadir}/icons/hicolor >&/dev/null || :
fi

%posttrans 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%{_datadir}/applications/helm.desktop

%files common
%{_datadir}/icons/hicolor/*
%{_bindir}/*
%{_datadir}/helm/*
%{_datadir}/doc/helm/*
%{_mandir}/man1/helm.1.gz

%files -n lv2-helm
%{_libdir}/lv2/*

%files -n vst-helm
%{_libdir}/vst/*

%changelog
* Fri Jul 5 2019 Drew DeVore <drew@devorcula.com> - master
- updated naming scheme to fit Fedora git standards and updated description

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 20180608git
- update for Fedora 29

* Sat Aug 11 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-3
- update to abdedd527e6e1cf86636f0f1e8a3e75b06ed166a

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-2
- update to 756e767e4d20e77836f45b4ba016ea547d7cf474 

* Mon Oct 23 2017 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta-1
- update to latest master

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 1.0.0beta
- Initial build

