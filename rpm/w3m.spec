Name:           w3m
Version:        0.5.3
Release:        1
Summary:        A pager with WWW capability
Url:            https://sourceforge.net/projects/w3m/
Source:         https://github.com/tats/w3m/
License:        MIT
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(bdw-gc)
#BuildRequires:  libgc
BuildRequires:  autoconf

%description
w3m is a pager with WWW capability. It IS a pager, but it can be used as a text-mode WWW browser.

%package docs
Summary:   w3m documentation package

%description docs
Documentation for w3m - a pager with WWW capability. It IS a pager, but it can be used as a text-mode WWW browser.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%configure
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/w3m

%files docs
%defattr(-,root,root)
%{_bindir}/w3mman
%{_libexecdir}/w3m/cgi-bin/dirlist.cgi
%{_libexecdir}/w3m/cgi-bin/multipart.cgi
%{_libexecdir}/w3m/cgi-bin/w3mbookmark
%{_libexecdir}/w3m/cgi-bin/w3mdict.cgi
%{_libexecdir}/w3m/cgi-bin/w3mhelp.cgi
%{_libexecdir}/w3m/cgi-bin/w3mhelperpanel
%{_libexecdir}/w3m/cgi-bin/w3mmail.cgi
%{_libexecdir}/w3m/cgi-bin/w3mman2html.cgi
%{_libexecdir}/w3m/inflate
%{_libexecdir}/w3m/w3mimgdisplay
%{_libexecdir}/w3m/xface2xpm
%{_mandir}/de/man1/*.gz
%{_mandir}/ja/man1/*.gz
%{_mandir}/man1/*.gz
%{_datadir}/w3m/*.pl
%{_datadir}/w3m/*.html

