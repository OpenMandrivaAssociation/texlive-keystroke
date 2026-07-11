%global tl_name keystroke
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Graphical representation of keys on keyboard
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keystroke
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keystroke.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package which provides macros for the graphical representation
of the keys on a computer keyboard.

