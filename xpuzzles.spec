Summary:	Geometric puzzles and toys for the X Window System
Summary(pl):	Geometryczne uk³adanki i zabawki pod X Window System
Name:		xpuzzles
Version:	5.5.2
Release:	5
License:	MIT
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/strategy/%{name}-%{version}.tar.gz
Patch0:		%{name}-5.4.1-install.patch
Patch1:		%{name}-5.4.1-nobr.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A set of geometric puzzles and toys for the X Window System. Xpuzzles
includes a version of Rubik's cube and various other geometric Rubik's
cube style puzzles.

%description -l pl
Zestaw geometrycznych uk³adanek i zabawek pod X Window System. Zawiera
wersjê kostki Rubika i ró¿ne inne uk³adanki w tym stylu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} -f xpuzzles.Makefile xmkmf
%{__make} -f xpuzzles.Makefile CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_applnkdir}/Games}

%{__make} -f xpuzzles.Makefile install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf xpuzzles.README

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xcubes.desktop <<EOF
[Desktop Entry]
Name=xcubes
Type=Application
Exec=xcubes
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xdino.desktop <<EOF
[Desktop Entry]
Name=xdino
Type=Application
Exec=xdino
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xhexagons.desktop <<EOF
[Desktop Entry]
Name=xhexagons
Type=Application
Exec=xhexagons
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xmball.desktop <<EOF
[Desktop Entry]
Name=xmball
Type=Application
Exec=xmball
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xmlink.desktop <<EOF
[Desktop Entry]
Name=xmlink
Type=Application
Exec=xmlink
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xoct.desktop <<EOF
[Desktop Entry]
Name=xoct
Type=Application
Exec=xoct
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xpanex.desktop <<EOF
[Desktop Entry]
Name=xpanex
Type=Application
Exec=xpanex
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xpyraminx.desktop <<EOF
[Desktop Entry]
Name=xpyraminx
Type=Application
Exec=xpyraminx
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xrubik.desktop <<EOF
[Desktop Entry]
Name=xskewb
Type=Application
Exec=xskewb
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xskewb.desktop <<EOF
[Desktop Entry]
Name=xskewb
Type=Application
Exec=xskewb
EOF

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xtriangles.desktop <<EOF
[Desktop Entry]
Name=xtriangles
Type=Application
Exec=xtriangles
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/Games/*.desktop
%attr(755,root,root) %{_bindir}/xpanex
%attr(755,root,root) %{_bindir}/xrubik
%attr(755,root,root) %{_bindir}/xskewb
%attr(755,root,root) %{_bindir}/xdino
%attr(755,root,root) %{_bindir}/xpyraminx
%attr(755,root,root) %{_bindir}/xoct
%attr(755,root,root) %{_bindir}/xmball
%attr(755,root,root) %{_bindir}/xcubes
%attr(755,root,root) %{_bindir}/xtriangles
%attr(755,root,root) %{_bindir}/xhexagons
%attr(755,root,root) %{_bindir}/xmlink
%{_mandir}/man1/xpanex.1*
%{_mandir}/man1/xrubik.1*
%{_mandir}/man1/xskewb.1*
%{_mandir}/man1/xdino.1*
%{_mandir}/man1/xpyraminx.1*
%{_mandir}/man1/xoct.1*
%{_mandir}/man1/xmball.1*
%{_mandir}/man1/xcubes.1*
%{_mandir}/man1/xtriangles.1*
%{_mandir}/man1/xhexagons.1*
%{_mandir}/man1/xmlink.1*
