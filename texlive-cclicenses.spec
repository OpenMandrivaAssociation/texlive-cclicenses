%global tl_name cclicenses
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset Creative Commons licence logos
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cclicenses
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cclicenses.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The cclicenses package helps users typesetting Creative Commons logos in
LaTeX. It defines some commands useful to quickly write these logos,
related to CC licences versions 1.0 and 2.0.

