# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cclicenses
# catalog-date 2008-08-17 13:56:26 +0200
# catalog-license lppl
# catalog-version undef
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cclicenses/cclicenses.sty
%doc %{_texmfdistdir}/doc/latex/cclicenses/README
%doc %{_texmfdistdir}/doc/latex/cclicenses/cclicenses_short.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cclicenses/cclicenses.dtx
%doc %{_texmfdistdir}/source/latex/cclicenses/cclicenses.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
