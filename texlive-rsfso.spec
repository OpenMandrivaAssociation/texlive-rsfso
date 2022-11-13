Name:		texlive-rsfso
Version:	60849
Release:	1
Summary:	A mathematical calligraphic font based on rsfs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/rsfso
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rsfso.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides virtual fonts and LaTeX support files for
mathematical calligraphic fonts based on the rsfs Adobe Type 1
fonts (which must also be present for successful installation,
with the slant substantially reduced. The output is quite
similar to that from the Adobe Mathematical Pi script font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/rsfso
%{_texmfdistdir}/fonts/tfm/public/rsfso
%{_texmfdistdir}/fonts/vf/public/rsfso
%{_texmfdistdir}/tex/latex/rsfso
%doc %{_texmfdistdir}/doc/fonts/rsfso

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
