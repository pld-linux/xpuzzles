Summary:	Geometric puzzles and toys for the X Window System
Summary(pl):	Geometryczne uk³adanki i zabawki pod X Window System
Name:		xpuzzles
Version:	7.0.1
Release:	7
License:	MIT
Group:		X11/Applications/Games
Source0:	http://www.tux.org/pub/tux/xpuzzles/%{name}-%{version}.tar.bz2
# Source0-md5:	391e4b300cf815d91aea228448647b48
Source1:	xbarrel.desktop
Source2:	xcubes.desktop
Source3:	xdino.desktop
Source4:	xhexagons.desktop
Source5:	xmball.desktop
Source6:	xmlink.desktop
Source7:	xoct.desktop
Source8:	xpanex.desktop
Source9:	xpyraminx.desktop
Source10:	xrubik.desktop
Source11:	xskewb.desktop
Source12:	xthreed.desktop
Source13:	xtriangles.desktop
Patch0:		%{name}-man.patch
URL:		http://www.tux.org/~bagleyd/puzzles.html
BuildRequires:	XFree86-devel
BuildRequires:	openmotif-devel
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
install -d $RPM_BUILD_ROOT/var/games/xpuzzles

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

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} \
	%{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} \
	%{SOURCE13} $RPM_BUILD_ROOT%{_desktopdir}

touch $RPM_BUILD_ROOT/var/games/xpuzzles/{barrel,cubes,dino,hexagons,mball,mlink,oct,panex,pyramix,rubik,skewb,threed,triangles}.scores

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 002
touch /var/games/xpuzzles/{barrel,cubes,dino,hexagons,mball,mlink,oct,panex,pyramix,rubik,skewb,threed,triangles}.scores
chgrp games /var/games/xpuzzles/{barrel,cubes,dino,hexagons,mball,mlink,oct,panex,pyramix,rubik,skewb,threed,triangles}.scores

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
%dir /var/games/xpuzzles
%attr(664,root,games) %ghost /var/games/xpuzzles/barrel.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/cubes.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/dino.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/hexagons.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/mball.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/mlink.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/oct.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/panex.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/pyramix.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/rubik.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/skewb.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/threed.scores
%attr(664,root,games) %ghost /var/games/xpuzzles/triangles.scores
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
