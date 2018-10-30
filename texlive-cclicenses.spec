# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cclicenses
# catalog-date 2008-08-17 13:56:26 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-cclicenses
Version:	20180303
Release:	3
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080817-2
+ Revision: 750043
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080817-1
+ Revision: 718020
- texlive-cclicenses
- texlive-cclicenses
- texlive-cclicenses
- texlive-cclicenses
- texlive-cclicenses

