%custom.cls

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{custom}[2024/12/20 My Custom Format]

% Base it on an existing class
\LoadClass[12 pt,a4 paper]{report}

% Load required packages
\RequirePackage{geometry}
\RequirePackage{title sec}
\RequirePackage{x color}

% Custom margins
\geometry{
    top=1 in,
    bottom=1 in,
    left=1.5 in,
    right=1 in
}

% Custom title formatting

\titleformat{\title}
  {\fontsize{12}{18}\selectfont\bfseries\setstretch{1.5}}
  {}{0 pt}{\MakeUppercase}

\titlespacing{\title}
  {0 pt}     % Left indent
  {0 pt}     % Space before
  {0 pt}    % Space after


% Custom chapter formatting
\usepackage{titlesec}
\usepackage{setspace}

\titleformat{\chapter}
  {\fontsize{12}{18}\selectfont\bfseries\setstretch{1.5}}
  {}{0 pt}{\MakeUppercase}

\titlespacing{\chapter}
  {0 pt}     % Left indent
  {0 pt}     % Space before
  {12 pt}    % Space after

\titleformat{\section}
  {\fontsize{12}{18}\selectfont\bfseries\setstretch{1.5}}
  {\thesection}{1 em}{}
  
\titlespacing{\section}
  {0 pt}     % Left indent
  {0 pt}     % Space before: 0
  {12 pt}    % Space after: 12pt

\titleformat{\subsection}
  {\fontsize{12}{18}\bfseries\setstretch{1.5}}
  {\thesubsection}{1 em}{}

\titlespacing{\subsection}
  {0 pt}
  {0 pt}
  {10 pt}

% NORMAL PARAGRAPH FORMATTING
% Font size: 12pt (already set by \LoadClass[12pt])
% Line spacing: 1.5
\setstretch{1.5}

% Spacing before: 0, after: 18pt
\setlength{\parskip}{18pt}      % 18pt space after each paragraph
\setlength{\parindent}{0pt}     % No indent (since we have space between paragraphs)
