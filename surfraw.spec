Summary:	Shell Users Revolutionary Front Rage Against the Web
Summary(pl.UTF-8):	SURFRAW - rewolucyjny front użytkowników shellowych przeciwko WWW
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

%description -l pl.UTF-8
Surfraw udostępnia szybki interfejs z uniksowej linii poleceń do wielu
popularnych silników wyszukiwarek WWW i innych artefaktów siły. Czyści
serwisy google, altavista, dejanews, freshmeat, research index,
slashdot oraz wiele innych od fałszywych, nawiedzonych zarazą terenów
formularzy HTML, umieszczając te dziwy tam, gdzie ich miejsce - głęboko
w wewnętrznych krainach Uniksa, tak jak rozszerzenia powłoki.

Surfraw absrahuje przeglądarkę od wejścia, co pozwala jej otrzymać to,
w czym jest dobra - przeglądanie. Interpretowanie formularzy
językowych jest obsługiwane przez powłokę. W połączeniu z
przyrostowymi przeglądarkami tekstowymi, takimi jak links, w3m (czy
nawet lynx) oraz screenem, lub netscape-remote wyzwoleniec Surfraw
może wyszukiwać z prędkościami pozostawiającymi napiętnowanych
heretyków używających GUI w strachu i zwątpieniu.

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
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}*
