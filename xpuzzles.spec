Summary: Geometric puzzles and toys for the X Window System.
Name: xpuzzles
Version: 5.4.1
Release: 7
Copyright: MIT
Group: Amusements/Games
Source: ftp://sunsite.unc.edu/pub/Linux/games/strategy/xpuzzles-5.4.1.tgz
Patch: xpuzzles-5.4.1-install.patch
Patch1: xpuzzles-5.4.1-nobr.patch
BuildRoot: /var/tmp/xpuzzles-root

%description
A set of geometric puzzles and toys for the X Window System.  Xpuzzles
includes a version of Rubik's cube and various other geometric Rubik's
cube style puzzles.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .nobr

%build
make -f xpuzzles.Makefile xmkmf
make -f xpuzzles.Makefile

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/{bin,man/man1}

make -f xpuzzles.Makefile DESTDIR=$RPM_BUILD_ROOT install

strip $RPM_BUILD_ROOT/usr/X11R6/bin/* 

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
%defattr(-,root,root)
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

/usr/X11R6/bin/xpanex
/usr/X11R6/man/man1/xpanex.1
/usr/X11R6/bin/xrubik
/usr/X11R6/man/man1/xrubik.1
/usr/X11R6/bin/xskewb
/usr/X11R6/man/man1/xskewb.1
/usr/X11R6/bin/xdino
/usr/X11R6/man/man1/xdino.1
/usr/X11R6/bin/xpyraminx
/usr/X11R6/man/man1/xpyraminx.1
/usr/X11R6/bin/xoct
/usr/X11R6/man/man1/xoct.1
/usr/X11R6/bin/xmball
/usr/X11R6/man/man1/xmball.1
/usr/X11R6/bin/xcubes
/usr/X11R6/man/man1/xcubes.1
/usr/X11R6/bin/xtriangles
/usr/X11R6/man/man1/xtriangles.1
/usr/X11R6/bin/xhexagons
/usr/X11R6/man/man1/xhexagons.1
/usr/X11R6/bin/xmlink
/usr/X11R6/man/man1/xmlink.1
