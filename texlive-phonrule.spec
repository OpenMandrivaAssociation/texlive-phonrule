# revision 31966
# category Package
# catalog-ctan /macros/latex/contrib/phonrule
# catalog-date 2013-10-21 18:32:18 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-phonrule
Version:	0.01
Release:	4
Summary:	Typeset linear phonological rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phonrule
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonrule.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phonrule.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting phonological rules
like those in 'Sound Pattern of English' (Chomsky and Halle
1968).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/phonrule/phonrule.sty
%doc %{_texmfdistdir}/doc/latex/phonrule/README
%doc %{_texmfdistdir}/doc/latex/phonrule/phonrule-doc.pdf
%doc %{_texmfdistdir}/doc/latex/phonrule/phonrule-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
