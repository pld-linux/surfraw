Summary:	Shell Users Revolutionary Front Rage Against the Web
Summary(pl):	SURFRAW - rewolucyjny front u�ytkownik�w shellowych przeciwko WWW
Name:		surfraw
Version:	1.0.7
Release:	3
License:	Public Domain
Group:		Applications/Console
Source0:	ftp://ftp.netbsd.org/pub/NetBSD/misc/proff/%{name}-%{version}.tar.gz
# Source0-md5:	0957382bbdebf3d678879fa5d2592c9d
Patch0:		%{name}-autoconf.patch
URL:		http://surfraw.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	webclient
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Surfraw provides a fast unix command line interface to a variety of
popular WWW search engines and other artifacts of power. It reclaims
google, altavista, dejanews, freshmeat, research index, slashdot and
many others from the false-prophet, pox-infested heathen lands of
html-forms, placing these wonders where they belong, deep in unix
heartland, as god loving extensions to the shell.

Surfraw abstracts the browser away from input. Doing so lets it get on
with what it's good at. Browsing. Interpretation of linguistic forms
is handed back to the shell, which is what it, and human beings are
good at. Combined with incremental text browsers, such as links, w3m
(or even lynx), and screen(1), or netscape-remote a Surfraw liberateur
is capable of research speeds that leave GUI tainted idolaters agape
with fear and wonder.

%description -l pl
Surfraw udost�pnia szybki interfejs z uniksowej linii polece� do wielu
popularnych silnik�w wyszukiwarek WWW i innych artefakt�w si�y. Czy�ci
serwisy google, altavista, dejanews, freshmeat, research index,
slashdot oraz wiele innych od fa�szywych, nawiedzonych zaraz� teren�w
formularzy HTML, umieszczaj�c te dziwy tam, gdzie ich miejsce - g��boko
w wewn�trznych krainach Uniksa, tak jak rozszerzenia pow�oki.

Surfraw absrahuje przegl�dark� od wej�cia, co pozwala jej otrzyma� to,
w czym jest dobra - przegl�danie. Interpretowanie formularzy
j�zykowych jest obs�ugiwane przez pow�ok�. W po��czeniu z
przyrostowymi przegl�darkami tekstowymi, takimi jak links, w3m (czy
nawet lynx) oraz screenem, lub netscape-remote wyzwoleniec Surfraw
mo�e wyszukiwa� z pr�dko�ciami pozostawiaj�cymi napi�tnowanych
heretyk�w u�ywaj�cych GUI w strachu i zw�tpieniu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS HACKING TODO NEWS COPYING
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}*