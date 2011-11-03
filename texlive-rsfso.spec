# revision 23462
# category Package
# catalog-ctan /fonts/rsfso
# catalog-date 2011-02-18 16:44:14 +0100
# catalog-license lppl
# catalog-version 1
Name:		texlive-rsfso
Version:	1
Release:	1
Summary:	A mathematical calligraphic font based on rsfs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/rsfso
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1
fonts (which must also be present for successful installation,
with the slant substantially reduced. The output is quite
similar to that from the Adobe Mathematical Pi script font.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/rsfso/rsfso.map
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rrsfso7.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso10.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso5.tfm
%{_texmfdistdir}/fonts/tfm/public/rsfso/rsfso7.tfm
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso10.vf
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso5.vf
%{_texmfdistdir}/fonts/vf/public/rsfso/rsfso7.vf
%{_texmfdistdir}/tex/latex/public/rsfso/rsfso.sty
%{_texmfdistdir}/tex/latex/public/rsfso/ursfso.fd
%doc %{_texmfdistdir}/doc/fonts/rsfso/README
%doc %{_texmfdistdir}/doc/fonts/rsfso/mh2scr0.png
%doc %{_texmfdistdir}/doc/fonts/rsfso/rsfso-doc.pdf
%doc %{_texmfdistdir}/doc/fonts/rsfso/rsfso-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
