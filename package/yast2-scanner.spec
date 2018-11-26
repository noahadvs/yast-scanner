#
# spec file for package yast2-scanner
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-scanner
Version:        4.0.3
Release:        0
Group:		System/YaST

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:	docbook-xsl-stylesheets doxygen libxslt perl-XML-Writer sgml-skel update-desktop-files xorg-x11-libX11-devel yast2 yast2-testsuite libtool
BuildRequires:  yast2-devtools >= 3.1.10
Requires:	yast2
# Used to exclude libX11, libXau, libxcb, and libxcb-xlib from the requires list
# which are pulled in by Autoreqprov because of the displaytest tool:
%define my_requires /tmp/my-requires

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:	YaST2 - Scanner Configuration
License:        GPL-2.0-only

%description
This package provides support for the configuration of USB scanners,
SCSI scanners, scanners in HP all-in-one devices, and scanning via
network (i.e. use a remote scanner via another host in the network).

Parallel port scanners and network scanners (i.e. a scanner which is
directly accessible in the network) cannot be configured with this
tool, except for such scanners in HP all-in-one devices. Usually those
devices must be configured manually. For more information see
http://www.sane-project.org/ and the documentation in the package
"sane-backends".

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

# Exclude libX11, libXau, libxcb, and libxcb-xlib from the requires list
# which are pulled in by Autoreqprov because of the displaytest tool:
cat << EOF > %{my_requires}
grep -v 'displaytest' | %{__find_requires}
EOF
chmod 755 %{my_requires}
%define __find_requires %{my_requires}


%files
%defattr(-,root,root)
%dir %{yast_yncludedir}/scanner
%{yast_yncludedir}/scanner/*
%{yast_clientdir}/scanner.rb
%{yast_moduledir}/Scanner.*
%{yast_desktopdir}/scanner.desktop
%{yast_ybindir}/*scanner*
%{yast_ybindir}/displaytest
%{_datadir}/icons/*
%doc %{yast_docdir}
%license COPYING

%changelog

