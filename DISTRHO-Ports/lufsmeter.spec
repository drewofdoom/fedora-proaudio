%global debug_package %{nil}

Name:           lv2-lufsmeter
Version:        20180416git
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        A LUFS meter

Group:          Applications/Multimedia
License:        MIT
URL:            https://www.airwindows.com/
Source0:        https://github.com/DISTRHO/DISTRHO-Ports/releases/download/2018-04-16/lufsmeter-linux64.tar.xz

%description
A LUFS meter

%package -n vst-lufsmeter
Summary:        A LUFS meter
Group:          Applications/Multimedia
Requires:       %{name}-common = %{version}-%{release}

%description -n vst-lufsmeter
A LUFS meter

%prep
%autosetup -n lufsmeter-linux64

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{_libdir}/lv2/LUFSMeter.lv2
mkdir -p %{buildroot}%{_libdir}/lv2/LUFSMeterMulti.lv2
mkdir -p %{buildroot}%{_libdir}/vst/
install -p -m 744 LUFSMeter.lv2/* %{buildroot}%{_libdir}/lv2/LUFSMeter.lv2/
install -p -m 744 LUFSMeterMulti.lv2/* %{buildroot}%{_libdir}/lv2/LUFSMeterMulti.lv2/
install -p -m 744 *.so %{buildroot}%{_libdir}/vst/

%clean

%files
%{_libdir}/lv2/LUFSMeter.lv2
%{_libdir}/lv2/LUFSMeterMulti.lv2

%files -n vst-lufsmeter
%{_libdir}/vst/

%changelog
* Fri Feb 28 2020 Drew DeVore <drew@devorcula.com> - 20200223
- initial build