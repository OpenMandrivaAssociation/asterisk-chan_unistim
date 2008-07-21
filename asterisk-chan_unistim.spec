%define rname	chan_unistim

Summary:	This module adds Unistim protocol support to the Asterisk PBX
Name:		asterisk-%{rname}
Version:	0.9.4
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://www.mlkj.net/UNISTIM/
Source0:	http://www.mlkj.net/asterisk/%{rname}-%{version}.tar.bz2
BuildRequires:	asterisk-devel >= 1.2
Requires:	asterisk >= 1.2
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This is a channel driver for Unistim protocol. You can use a least
a Nortel i2004 phone with it. Only few features are supported :
Send/Receive CallerID, Redial, SoftKeys, SendText(), Music On Hold,
Message Waiting Indication (MWI).

%prep

%setup -q -n %{rname}-%{version}

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done
    
# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

%build

make CFLAGS="%{optflags} -pipe -Wall -fPIC -DPIC -D_REENTRANT -D_GNU_SOURCE"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/asterisk
install -d %{buildroot}%{_libdir}/asterisk

install -m0644 unistim.conf %{buildroot}%{_sysconfdir}/asterisk/
install -m0755 chan_unistim.so %{buildroot}%{_libdir}/asterisk/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/asterisk/unistim.conf
%attr(0755,root,root) %{_libdir}/asterisk/chan_unistim.so

