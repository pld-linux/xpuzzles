Summary:	Geometric puzzles and toys for the X Window System
Summary(pl):	Geometryczne uk³adanki i zabawki pod X Window System
Name:		xpuzzles
Version:	7.0.1
Release:	2
License:	MIT
Group:		X11/Applications/Games
Source0:	http://www.tux.org/pub/tux/xpuzzles/%{name}-%{version}.tar.bz2
# Source0-md5:	391e4b300cf815d91aea228448647b48
URL:		http://www.tux.org/~bagleyd/puzzles.html
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of geometric puzzles and toys for the X Window System. Xpuzzles
includes a version of Rubik's cube and various other geometric Rubik's
cube style puzzles.

%description -l pl
Zestaw geometrycznych uk³adanek i zabawek pod X Window System. Zawiera
wersjê kostki Rubika i ró¿ne inne uk³adanki w tym stylu.

%prep
%setup -q

%build
%{__make} -f xpuzzles.Makefile xmkmf
%{__make} -f xpuzzles.Makefile \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	XMDEF="-DHAVE_MOTIF" \
	XMLIB="-lXm"

# not included in xpuzzles.Makefile
cd xthreed
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	XMDEF="-DHAVE_MOTIF" \
	XMLIB="-lXm" \
	DATAFILE="%{_datadir}/misc/xthreed.dat"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -f xpuzzles.Makefile install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

# not included in xpuzzles.Makefile
%{__make} -C xthreed install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}
install -D xthreed/threed.dat $RPM_BUILD_ROOT%{_datadir}/misc/xthreed.dat

for d in `find . -type d -maxdepth 1 -mindepth 1 | grep -v xdial` ; do
	%{__make} -C $d install.man \
		DESTDIR=$RPM_BUILD_ROOT \
		MANDIR=%{_mandir}/man1
done

cat > $RPM_BUILD_ROOT%{_desktopdir}/xbarrel.desktop <<EOF
[Desktop Entry]
Name=xbarrel
Type=Application
Exec=xbarrel
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xcubes.desktop <<EOF
[Desktop Entry]
Name=xcubes
Type=Application
Exec=xcubes
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xdino.desktop <<EOF
[Desktop Entry]
Name=xdino
Type=Application
Exec=xdino
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xhexagons.desktop <<EOF
[Desktop Entry]
Name=xhexagons
Type=Application
Exec=xhexagons
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xmball.desktop <<EOF
[Desktop Entry]
Name=xmball
Type=Application
Exec=xmball
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xmlink.desktop <<EOF
[Desktop Entry]
Name=xmlink
Type=Application
Exec=xmlink
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xoct.desktop <<EOF
[Desktop Entry]
Name=xoct
Type=Application
Exec=xoct
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xpanex.desktop <<EOF
[Desktop Entry]
Name=xpanex
Type=Application
Exec=xpanex
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xpyraminx.desktop <<EOF
[Desktop Entry]
Name=xpyraminx
Type=Application
Exec=xpyraminx
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xrubik.desktop <<EOF
[Desktop Entry]
Name=xskewb
Type=Application
Exec=xskewb
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xskewb.desktop <<EOF
[Desktop Entry]
Name=xskewb
Type=Application
Exec=xskewb
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xthreed.desktop << EOF
[Desktop Entry]
Name=xthreed
Type=Application
Exec=xthreed
Categories=Game;
EOF

cat > $RPM_BUILD_ROOT%{_desktopdir}/xtriangles.desktop <<EOF
[Desktop Entry]
Name=xtriangles
Type=Application
Exec=xtriangles
Categories=Game;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xpuzzles.README
%attr(755,root,root) %{_bindir}/xbarrel
%attr(755,root,root) %{_bindir}/xcubes
%attr(755,root,root) %{_bindir}/xdino
%attr(755,root,root) %{_bindir}/xhexagons
%attr(755,root,root) %{_bindir}/xmball
%attr(755,root,root) %{_bindir}/xmlink
%attr(755,root,root) %{_bindir}/xoct
%attr(755,root,root) %{_bindir}/xpanex
%attr(755,root,root) %{_bindir}/xpyraminx
%attr(755,root,root) %{_bindir}/xrubik
%attr(755,root,root) %{_bindir}/xskewb
%attr(755,root,root) %{_bindir}/xthreed
%attr(755,root,root) %{_bindir}/xtriangles
%{_datadir}/misc/xthreed.dat
%{_desktopdir}/*.desktop
%{_mandir}/man1/xbarrel.1*
%{_mandir}/man1/xcubes.1*
%{_mandir}/man1/xdino.1*
%{_mandir}/man1/xhexagons.1*
%{_mandir}/man1/xmball.1*
%{_mandir}/man1/xmlink.1*
%{_mandir}/man1/xoct.1*
%{_mandir}/man1/xpanex.1*
%{_mandir}/man1/xpyraminx.1*
%{_mandir}/man1/xrubik.1*
%{_mandir}/man1/xskewb.1*
%{_mandir}/man1/xthreed.1*
%{_mandir}/man1/xtriangles.1*
