Summary:	Geometric puzzles and toys for the X Window System.
Name:		xpuzzles
Version:	5.4.1
Release:	7
Copyright:	MIT
Group:		Amusements/Games
Source:		ftp://sunsite.unc.edu/pub/Linux/games/strategy/%{name}-%{version}.tgz
Patch:		xpuzzles-5.4.1-install.patch
Patch1:		xpuzzles-5.4.1-nobr.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A set of geometric puzzles and toys for the X Window System.  Xpuzzles
includes a version of Rubik's cube and various other geometric Rubik's
cube style puzzles.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make -f xpuzzles.Makefile xmkmf
make -f xpuzzles.Makefile CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make -f xpuzzles.Makefile install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* 

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xcubes <<EOF
xcubes name "xcubes"
xcubes description "xcubes"
xcubes group Games/Strategy
xcubes exec "xcubes &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xdino <<EOF
xdino name "xdino"
xdino description "xdino"
xdino group Games/Strategy
xdino exec "xdino &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xhexagons <<EOF
xhexagons name "xhexagons"
xhexagons description "xhexagons"
xhexagons group Games/Strategy
xhexagons exec "xhexagons &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmball <<EOF
xmball name "xmball"
xmball description "xmball"
xmball group Games/Strategy
xmball exec "xmball &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xmlink <<EOF
xmlink name "xmlink"
xmlink description "xmlink"
xmlink group Games/Strategy
xmlink exec "xmlink &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xoct <<EOF
xoct name "xoct"
xoct description "xoct"
xoct group Games/Strategy
xoct exec "xoct &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpanex <<EOF
xpanex name "xpanex"
xpanex description "xpanex"
xpanex group Games/Strategy
xpanex exec "xpanex &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xpyraminx <<EOF
xpyraminx name "xpyraminx"
xpyraminx description "xpyraminx"
xpyraminx group Games/Strategy
xpyraminx exec "xpyraminx &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xrubik <<EOF
xrubik name "xrubik"
xrubik description "xrubik"
xrubik group Games/Strategy
xrubik exec "xrubik &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xskewb <<EOF
xskewb name "xskewb"
xskewb description "xskewb"
xskewb group Games/Strategy
xskewb exec "xskewb &"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xtriangles <<EOF
xtriangles name "xtriangles"
xtriangles description "xtriangles"
xtriangles group Games/Strategy
xtriangles exec "xtriangles &"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config /etc/X11/wmconfig/xcubes
%config /etc/X11/wmconfig/xdino
%config /etc/X11/wmconfig/xhexagons
%config /etc/X11/wmconfig/xmball
%config /etc/X11/wmconfig/xmlink
%config /etc/X11/wmconfig/xoct
%config /etc/X11/wmconfig/xpanex
%config /etc/X11/wmconfig/xpyraminx
%config /etc/X11/wmconfig/xrubik
%config /etc/X11/wmconfig/xskewb
%config /etc/X11/wmconfig/xtriangles
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
%{_mandir}/man1/xpanex.1.gz
%{_mandir}/man1/xrubik.1.gz
%{_mandir}/man1/xskewb.1.gz
%{_mandir}/man1/xdino.1.gz
%{_mandir}/man1/xpyraminx.1.gz
%{_mandir}/man1/xoct.1.gz
%{_mandir}/man1/xmball.1.gz
%{_mandir}/man1/xcubes.1.gz
%{_mandir}/man1/xtriangles.1.gz
%{_mandir}/man1/xhexagons.1.gz
%{_mandir}/man1/xmlink.1.gz
