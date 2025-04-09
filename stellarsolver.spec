%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:        Astrometric Solver
Name:           stellarsolver
Version:        2.6
Release:        1
License:        GPL-3.0-only
Group:          Graphical desktop/KDE
URL:            https://github.com/rlancaste/stellarsolver
Source0:        https://github.com/rlancaste/stellarsolver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ninja
BuildRequires:  qmake-qt6
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(wcslib)
# adapt uptram patch for get rid of system qsort
#		https://github.com/dstndstn/astrometry.net/commit/1d112038134b79f019ee5d557680a53c36a6cf42
#Patch0:		stellarsolver-2.4-fix_qsort.patch
BuildSystem:	cmake
BuildOption:	-DUSE_QT5:BOOL=OFF

%patchlist
stellarsolver-2.6-compile.patch

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

%files -n %{libname}
%{_libdir}/libstellarsolver.so.%{major}*

%files -n %{devname}
%license LICENSE
%{_includedir}/libstellarsolver/
%{_libdir}/cmake/StellarSolver/
%{_libdir}/libstellarsolver.so
%{_libdir}/pkgconfig/stellarsolver.pc
