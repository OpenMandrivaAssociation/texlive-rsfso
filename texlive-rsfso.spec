%global tl_name rsfso
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.03
Release:	%{tl_revision}.1
Summary:	A mathematical calligraphic font based on rsfs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/rsfso
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1 fonts
(which must also be present for successful installation, with the slant
substantially reduced. The output is quite similar to that from the
Adobe Mathematical Pi script font.

