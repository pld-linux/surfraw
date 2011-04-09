Summary:	Shell Users Revolutionary Front Rage Against the Web
Summary(pl.UTF-8):	SURFRAW - rewolucyjny front użytkowników shellowych przeciwko WWW
Name:		surfraw
Version:	2.2.7
Release:	2
License:	Public Domain
Group:		Applications/Console
Source0:	http://surfraw.alioth.debian.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	213010e9b7c8478827e8903530cf7787
URL:		http://surfraw.alioth.debian.org/
Patch0:		%{name}-gzlinks.patch
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	webclient
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Surfraw provides a fast Unix command line interface to a variety of
popular WWW search engines and other artifacts of power. It reclaims
google, altavista, dejanews, freshmeat, research index, slashdot and
many others from the false-prophet, pox-infested heathen lands of
html-forms, placing these wonders where they belong, deep in Unix
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
%patch0 -p0

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --libdir=%{_prefix}/lib
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
%dir %{_prefix}/lib/%{name}
%attr(755,root,root) %{_prefix}/lib/%{name}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/xdg/%{name}
%{_mandir}/man1/*.1*
