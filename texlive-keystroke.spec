# revision 17992
# category Package
# catalog-ctan /macros/latex/contrib/keystroke
# catalog-date 2010-04-23 13:36:14 +0200
# catalog-license gpl
# catalog-version v1.6
Name:		texlive-keystroke
Version:	v1.6
Release:	1
Summary:	Graphical representation of keys on keyboard
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keystroke
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A LaTeX package which provides macros for the graphical
representation of the keys on a computer keyboard.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
