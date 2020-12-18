%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:        Astrometric Solver
Name:           stellarsolver
Version:        1.5
Release:        1
License:        GPL-3.0-only
Group:          Graphical desktop/KDE
URL:            https://github.com/rlancaste/stellarsolver
Source0:        https://github.com/rlancaste/stellarsolver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ninja
BuildRequires:  qmake5
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(wcslib)

%description
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor).

%package -n %{libname}
Summary:        Astrometric Solver runtime library
Group:          System/Libraries

%description  -n %{libname}
An Astrometric Plate Solver for Mac, Linux, and Windows,
built on Astrometry.net and SEP (sextractor), runtime library.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
Development headers and libraries for %{name}.

%prep
%autosetup -p1

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libstellarsolver.so.%{major}*

%files -n %{devname}
%license LICENSE
%{_includedir}/libstellarsolver/
%{_libdir}/cmake/StellarSolver/
%{_libdir}/libstellarsolver.so
%{_libdir}/pkgconfig/stellarsolver.pc
