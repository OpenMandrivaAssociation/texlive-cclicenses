Name:		texlive-cclicenses
Version:	20080817
Release:	1
Summary:	Typeset Creative Commons licence logos
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cclicenses
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The cclicenses package helps users typesetting Creative Commons
logos in LaTeX. It defines some commands useful to quickly
write these logos, related to CC licences versions 1.0 and 2.0.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
