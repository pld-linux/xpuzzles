Summary:	Geometric puzzles and toys for the X Window System
Summary(pl):	Geometryczne uk³adanki i zabawki pod X Window System
Name:		xpuzzles
Version:	5.6.2
Release:	1
License:	MIT
Group:		Applications/Games
Source0:	ftp://sunsite.unc.edu/pub/Linux/games/strategy/%{name}-%{version}.tar.gz
Patch0:		%{name}-link.patch
BuildRequires:	XFree86-devel
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
%patch0 -p1

%build
%{__make} -f xpuzzles.Makefile xmkmf
%{__make} -f xpuzzles.Makefile \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

# not included in xpuzzles.Makefile
cd xthreed
xmkmf
%{__make} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	DATAFILE="%{_datadir}/misc/xthreed.dat"
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

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

cat > $RPM_BUILD_ROOT%{_applnkdir}/Games/xthreed.desktop << EOF
[Desktop Entry]
Name=xthreed
Type=Application
Exec=xthreed
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
%doc xpuzzles.README
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
%attr(755,root,root) %{_bindir}/xthreed
%{_datadir}/misc/xthreed.dat
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
%{_mandir}/man1/xthreed.1*
