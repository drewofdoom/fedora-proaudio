%global debug_package %{nil}

Name:           lv2-distrho-ports
Version:        20180416git
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        A collection of LV2 plugins

Group:          Applications/Multimedia
License:        MIT
URL:            https://github.com/DISTRHO/DISTRHO-Ports
Source0:        https://github.com/DISTRHO/DISTRHO-Ports/releases/download/2018-04-16/DISTRHO-Ports-2018-04-16-linux64.tar.xz

%description
A collection of LV2 plugins

%package -n vst-distrho-ports
Summary:        A collection of VST plugins
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}

%description -n vst-distrho-ports
A collection of VST plugins

%prep
%autosetup -n DISTRHO-Ports-linux64

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_libdir}/lv2/
mkdir -p %{buildroot}%{_libdir}/vst/
mv lv2/* %{buildroot}%{_libdir}/lv2/
install -p -m 744 vst/*.so %{buildroot}%{_libdir}/vst/

%clean

%files
%{_libdir}/lv2/

%files -n vst-distrho-ports
%{_libdir}/vst/

%changelog
* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 20200223
- initial build