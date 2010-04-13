%define		template	varnish
Summary:	Varnish Cache statistics template for Cacti
Name:		cacti-template-%{template}
Version:	0.0.3
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source1:	get_varnish_stats.py
Source2:	cacti_host_template_varnish.xml
URL:		http://forums.cacti.net/viewtopic.php?p=182152
BuildRequires:	unrar
Requires:	cacti >= 0.8.6j
Requires:	cacti-add_template
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		resourcedir		%{cactidir}/resource
%define		scriptsdir		%{cactidir}/scripts

%description
Template for Cacti - Varnish Cache statistics.

Uses advanced template from
<http://forums.cacti.net/viewtopic.php?p=182152>

Combines script to pull data via varnish telnet port from
<http://forums.cacti.net/viewtopic.php?t=31260>

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{resourcedir},%{scriptsdir}}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{scriptsdir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{resourcedir}

%post
%{_sbindir}/cacti-add_template \
	%{resourcedir}/cacti_host_template_varnish.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{scriptsdir}/get_varnish_stats.py
%{resourcedir}/*.xml
