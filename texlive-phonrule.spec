Name:		texlive-phonrule
Version:	1.3.2
Release:	1
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
%{_texmfdistdir}/tex/latex/phonrule
%doc %{_texmfdistdir}/doc/latex/phonrule

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
