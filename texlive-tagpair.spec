Name:		texlive-tagpair
Version:	42138
Release:	2
Summary:	Word-by-word glosses, translations, and bibliographic attributions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tagpair
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpair.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tagpair.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides environments and commands for pairing
lines, bottom lines, and tagged lines, intended to be used in
particular for word-by-word glosses, translations, and
bibliographic attributions, respectively. This LaTeX package is
inspired by Marcel R. van der Goot's classic Plain TeX macros
in gloss.tex.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tagpair
%doc %{_texmfdistdir}/doc/latex/tagpair

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
