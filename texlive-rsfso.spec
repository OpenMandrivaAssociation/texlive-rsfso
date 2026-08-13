%global tl_name rsfso
%global tl_revision 79618
%global tl_version 1.03

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A mathematical calligraphic font based on rsfs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/rsfso
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1 fonts
(which must also be present for successful installation, with the slant
substantially reduced. The output is quite similar to that from the
Adobe Mathematical Pi script font.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from rsfso:
Map rsfso.map
TL_DROPIN_EOF
