Name:		texlive-cclicenses
Version:	15878
Release:	2
Summary:	Typeset Creative Commons licence logos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cclicenses
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cclicenses package helps users typesetting Creative Commons
logos in LaTeX. It defines some commands useful to quickly
write these logos, related to CC licences versions 1.0 and 2.0.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cclicenses/cclicenses.sty
%doc %{_texmfdistdir}/doc/latex/cclicenses/README
%doc %{_texmfdistdir}/doc/latex/cclicenses/cclicenses_short.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cclicenses/cclicenses.dtx
%doc %{_texmfdistdir}/source/latex/cclicenses/cclicenses.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
