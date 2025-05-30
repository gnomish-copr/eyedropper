%define lname   com.github.finefindus.eyedropper
%bcond_with     warp
%define sname   blueprint-compiler
%define sver    0.8.1
Name:           eyedropper
Version:        2.1.0
Release:        0
Summary:        Pick and format colors
License:        GPL-3.0-or-later
URL:            https://github.com/FineFindus/eyedropper
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
%if %{with warp}
Source1:        https://gitlab.gnome.org/jwestman/%{sname}/-/archive/v%{sver}/%{sname}-v%{sver}.tar.bz2
BuildRequires:  python3-gobject
Provides:       bundled(blueprint-compiler)
%else
BuildRequires:  blueprint-compiler
%endif
BuildRequires:  libappstream-glib-devel
BuildRequires:  cargo-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.7.0
BuildRequires:  desktop-file-utils

%description
An application to pick and format colors.

Features:
- Pick a Color
- Enter a color in Hex-Format
- Parse RGB/RGBA/ARGB Hex-Colors
- View colors in formats
- Customize which formats appear as well as their order
- Generate a palette of different shades

%lang_package

%prep
%autosetup -p1
%if %{with warp}
mkdir subprojects/%{sname}
tar -xf %{SOURCE1} --strip-components 1 -C subprojects/%{sname}
%endif

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/%{name}
%{_datadir}/applications/%{lname}.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/%{lname}.gschema.xml
%{_datadir}/dbus-1/services/%{lname}.SearchProvider.service
%dir %{_datadir}/gnome-shell/
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{lname}.search-provider.ini
%{_datadir}/icons/hicolor/*/apps/%{lname}*.svg
%{_datadir}/metainfo/%{lname}.metainfo.xml

%files lang -f %{name}.lang

%changelog
