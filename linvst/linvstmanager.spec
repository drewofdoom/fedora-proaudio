%global debug_package %{nil}

Name:           linvstmanager
Version:        1.1.1
Release:        1%{?dist}
ExclusiveArch:  x86_64
Summary:        Manages LinVst wrapped windows VSTs

Group:          Applications/Multimedia
License:        GPLv3
URL:            https://github.com/Goli4thus/linvstmanager
Source0:        https://github.com/Goli4thus/linvstmanager/archive/v%{version}.zip#/linvstmanager-%{version}.zip
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  qt5-qtbase-devel

%description
Manages LinVst wrapped windows VSTs

%prep
%autosetup -n linvstmanager-%{version}

%build
mkdir build
cd build
cmake ..
make -j4

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/applications
install -p -m 755 build/linvstmanager %{buildroot}/%{_bindir}
install -p -m 744 build/linvstmanager.desktop %{buildroot}/%{_datadir}/applications

%clean

%files 
%{_bindir}/linvstmanager
%{_datadir}/applications/linvstmanager.desktop

%changelog
* Sun May 3 2020 Drew DeVore <drew@devorcula.com> - 1.1.1
- Updated to 1.0.2
* Fri May 1 2020 Drew DeVore <drew@devorcula.com> - 1.0.2
- Updated to 1.0.2
* Fri Mar 6 2020 Drew DeVore <drew@devorcula.com> - 1.0.1
- Initial version
