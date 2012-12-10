%define gnome_python2_version 1.99.13

Name:		gnome-blog
Summary:	GNOME panel object for posting blog entries
Version: 	0.9.2
Release:	%mkrel 3
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



%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.9.2-3mdv2011.0
+ Revision: 677711
- rebuild to add gconftool as req

* Sun Nov 07 2010 Jani Välimaa <wally@mandriva.org> 0.9.2-2mdv2011.0
+ Revision: 594851
- rebuild for python 2.7

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.1
+ Revision: 519806
- new version
- depend on python-gdata
- update license
- update file list

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-5mdv2010.0
+ Revision: 437758
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.9.1-4mdv2009.1
+ Revision: 325278
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-3mdv2009.0
+ Revision: 222290
- this package is not noarch
- fix file list on x86_64
- fix duplicated files in filelist
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Feb 12 2007 Jérôme Soyer <saispo@mandriva.org> 0.9.1-2mdv2007.0
+ Revision: 120014
- Fix python policies
- Fix python policies
- Fix python policies
- Fix BR
- Rebuild for latest python
- Import gnome-blog

* Fri Jun 23 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.1-1mdv2007.0
- Release 0.9.1
- use new macros

* Thu Aug 18 2005 Eskild Hustvedt <eskild@mandriva.org> 0.9-4mdk
- Requires gnome-python-gnomevfs
- %%mkrel

* Wed Apr 13 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.9-3mdk
- fix buildrequires

* Tue Apr 12 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.9-2mdk
- make it noarch
- fix buildrequires

* Fri Apr 01 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9-1mdk 
- Release 0.9

* Tue Mar 29 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-3mdk 
- Fix .server file
- Uninstall schema when removing package

* Tue Feb 08 2005 Jerome Soyer <saispo@mandrake.org> 0.8-2mdk
- Ooops fix spec error !

* Tue Feb 08 2005 Jerome Soyer <saispo@mandrake.org> 0.8-1mdk
- New release

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.7-2mdk
- Rebuild for new python

