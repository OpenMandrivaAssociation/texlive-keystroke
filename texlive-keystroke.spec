Name:		texlive-keystroke
Version:	17992
Release:	2
Summary:	Graphical representation of keys on keyboard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keystroke
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package which provides macros for the graphical
representation of the keys on a computer keyboard.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/keystroke/keystroke.sty
%{_texmfdistdir}/tex/latex/keystroke/keystroke_left.eps
%{_texmfdistdir}/tex/latex/keystroke/keystroke_left.pdf
%{_texmfdistdir}/tex/latex/keystroke/keystroke_middle.eps
%{_texmfdistdir}/tex/latex/keystroke/keystroke_middle.pdf
%{_texmfdistdir}/tex/latex/keystroke/keystroke_right.eps
%{_texmfdistdir}/tex/latex/keystroke/keystroke_right.pdf
%doc %{_texmfdistdir}/doc/latex/keystroke/README
%doc %{_texmfdistdir}/doc/latex/keystroke/key-test.pdf
%doc %{_texmfdistdir}/doc/latex/keystroke/key-test.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
