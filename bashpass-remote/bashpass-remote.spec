Name:           bashpass-remote
Version:        1.0
Release:        1%{?dist}
Summary:        A wrapper for BashPass, which allows you to manage your BashPass passwords stored on a remote server.
BuildArch:      noarch

License:        MIT
URL:            https://github.com/AntonVanAssche/BashPass-Remote
Source0:        %{name}-%{version}.tar.gz

Requires:       bash openssh

%description
BashPass-Remote allows you to securely access your passwords on a remote server, such as a NAS.
This project is written in (pure) Bash and acts as a wrapper around SSH and BashPass.
With BashPass-Remote, you can use BashPass as if it were installed locally, while your passwords are stored remotely.

%prep
%setup -q

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

cp -r bashpass-remote %{buildroot}%{_bindir}/bashpass-remote
cp -r bashpass-remote.1.gz %{buildroot}%{_mandir}/man1/bashpass-remote.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/bashpass-remote

%doc
%{_mandir}/man1/bashpass-remote.1.gz
