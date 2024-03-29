%define 	name	gftp
%define 	version	2.0.19
%define 	release	1
%define 	serial	1
%define 	prefix	/usr

Summary: 	Multithreaded FTP client for X Windows
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	GPL
Group:		Applications/Internet
Url:		http://www.gftp.org/
Vendor:		Brian Masney <masneyb@gftp.org>
Source:		http://www.gftp.org/%{name}-%{version}.tar.gz
Packager:	Brian Masney <masneyb@gftp.org>
BuildRoot:	/var/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.2.3

%description
gFTP is a multithreaded FTP client for X Windows written using Gtk. It
features simultaneous downloads, resuming of interrupted file transfers, file 
transfer queues, downloading of entire directories, ftp proxy support, remote 
directory caching, passive and non-passive file transfers, drag-n-drop support,
bookmarks menu, stop button, and many more features.

%prep
%setup -q
CFLAGS=$RPM_OPT_FLAGS \
	./configure --prefix=%{prefix}

%build
make

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
make -e prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README TODO docs/USERS-GUIDE
%{prefix}/bin/gftp
%{prefix}/bin/gftp-gtk
%{prefix}/bin/gftp-text
%{prefix}/share/gftp
%{prefix}/share/applications/gftp.desktop
%{prefix}/share/pixmaps/gftp.png
%{prefix}/man/*/gftp.*
%{prefix}/share/locale/*/LC_MESSAGES/gftp.mo

