%define gnome_python2_version 1.99.13
%define version	0.9.1

Name:		gnome-blog
Summary:	GNOME panel object for posting blog entries
Version: 	0.9.1
Release:	%mkrel 2
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/~seth/gnome-blog/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Requires:	gnome-python-applet >= %{gnome_python2_version}
Requires:	gnome-python-gconf  >= %{gnome_python2_version}
Requires:	gnome-python-gnomevfs

BuildRequires:  pygtk2.0-devel >= %{gnome_python2_version}
BuildRequires: perl-XML-Parser
BuildRequires: ImageMagick
BuildRequires: desktop-file-utils
BuildArch: noarch

%description
GNOME panel object that allows convenient posting of blog entries to
any blog that supports the bloggerAPI.

%prep
%setup -q
 
%build

./configure --prefix=%_prefix --libdir=%_libdir --libexecdir=%_libdir --sysconfdir=%_sysconfdir
#remove generated files
rm -f GNOME_BlogApplet.server GNOME_BlogApplet.server.in 

%make

%install
rm -rf %{buildroot}

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

%find_lang %name

mkdir -p $RPM_BUILD_ROOT%{_menudir}/

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):\
        needs="X11" \
        section="Internet/Other" \
        title="Blog Entry Poster" \
        longtitle="Post an entry to a web log" \
        command="%{_bindir}/gnome-blog-poster" \
        icon="gnome-blog.png" \
        startup_notify="true" \
	xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Internet-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
install -m 644 %{buildroot}%{_datadir}/pixmaps/gnome-blog.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 %{buildroot}%{_datadir}/pixmaps/gnome-blog.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 %{buildroot}%{_datadir}/pixmaps/gnome-blog.png %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%define schemas gnomeblog

%post
%post_install_gconf_schemas %{schemas}
%{update_menus}

%preun 
%preun_uninstall_gconf_schemas %{schemas}

%postun
%{clean_menus}


%files -f %name.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL README 
%{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/applications/*.desktop
%{_libdir}/bonobo/servers/*.server
%{py_platsitedir}/gnomeblog/*
%{py_platsitedir}/gnomeblog/*.py
%{py_platsitedir}/gnomeblog/*.pyc
%{py_platsitedir}/gnomeblog/*.pyo
%{_libdir}/blog_applet.py
%{_menudir}/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


