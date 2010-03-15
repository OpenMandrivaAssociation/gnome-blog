%define gnome_python2_version 1.99.13

Name:		gnome-blog
Summary:	GNOME panel object for posting blog entries
Version: 	0.9.2
Release:	%mkrel 1
License:	GPLv3
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/~seth/gnome-blog/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	gnome-python-applet >= %{gnome_python2_version}
Requires:	gnome-python-gconf  >= %{gnome_python2_version}
Requires:	gnome-python-gnomevfs
Requires:	python-gdata

BuildRequires: pygtk2.0-devel >= %{gnome_python2_version}
BuildRequires: desktop-file-utils
BuildRequires: intltool

%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.

%prep
%setup -q
 
%build

%configure2_5x --prefix=%_prefix --libdir=%_libdir --libexecdir=%_libdir --sysconfdir=%_sysconfdir
#remove generated files
rm -f GNOME_BlogApplet.server GNOME_BlogApplet.server.in 

%make

%install
rm -rf %{buildroot}

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %name

%clean
rm -rf %{buildroot}

%define schemas gnomeblog

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %{schemas}
%{update_menus}
%endif

%preun 
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS TODO INSTALL README 
%{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/applications/*.desktop
%{_libdir}/bonobo/servers/*.server
%{py_puresitedir}/gnomeblog/*
%{_libdir}/blog_applet.py
%_datadir/icons/hicolor/*/apps/gnome-blog.*

