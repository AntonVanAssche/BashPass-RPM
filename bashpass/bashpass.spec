Name:           bashpass
Version:        3.1
Release:        1%{?dist}
Summary:        A command-line based password manager written in Bash.
BuildArch:      noarch

License:        MIT
URL:            https://github.com/AntonVanAssche/BashPass
Source0:        %{name}-%{version}.tar.gz

Requires:       bash git gnupg2 wl-clipboard xclip

%description
BashPass is a command-line based password manager written in Bash.
It uses GPG to encrypt/decrypt the files where the passwords are stored .
This means the passwords are 100% stored locally, so you don't have to trust a third party to store your passwords.

%prep
%setup -q

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}/etc/skel/.config/bashpass/

cp -r bashpass %{buildroot}%{_bindir}/bashpass
cp -r bashpass.conf %{buildroot}/etc/skel/.config/bashpass/bashpass.conf
cp -r bashpass.1.gz %{buildroot}%{_mandir}/man1/bashpass.1.gz
cp -r bashpass.conf.1.gz %{buildroot}%{_mandir}/man1/bashpass.conf.1.gz

%post
for user in /home/*; do
    mkdir -p /home/$user/.config/bashpass
    install -m 0644 /etc/skel/.config/bashpass/bashpass.conf /home/$user/.config/bashpass/bashpass.conf
done

%postun
for user in /home/*; do
    rm -rf /home/$user/.config/bashpass
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/bashpass

%doc
%{_mandir}/man1/bashpass.1.gz
%{_mandir}/man1/bashpass.conf.1.gz

%config(noreplace)
/etc/skel/.config/bashpass/bashpass.conf
